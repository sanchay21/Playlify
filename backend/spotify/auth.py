import os
from flask import make_response, redirect, request, Blueprint, jsonify, session, url_for
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, verify_jwt_in_request
import datetime
import requests
from dotenv import load_dotenv
from db import profile_col

import urllib.parse

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
FRONTEND_URL = os.getenv("FRONTEND_URL")

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1/'

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/")
def entry():
    try:
        verify_jwt_in_request()
        userid  = get_jwt_identity()
        if userid:
            return redirect(url_for('profile.me'))  
        else:
            return "Welcome to Playlify.<a href='/auth/login'> Login with Spotify></a>"
    except Exception as e: 
        print("JWT FAIL:", e)
        return redirect(url_for("auth.login"))
    
@auth_bp.route('/login')
def login():
    scope = 'user-top-read playlist-modify-private playlist-modify-public'

    params = {
        'client_id': SPOTIFY_CLIENT_ID,
        'response_type': 'code',
        'scope': scope,
        'redirect_uri': REDIRECT_URI,
        'show_dialog': True
    }

    return redirect(f"{AUTH_URL}?{urllib.parse.urlencode(params)}")



@auth_bp.route('/callback')
def callback():
    if 'error' in request.args:
        return jsonify({"error": request.args['error']})

    code = request.args.get('code')

    response = requests.post(
        TOKEN_URL,
        data={
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': REDIRECT_URI,
            'client_id': SPOTIFY_CLIENT_ID,
            'client_secret': SPOTIFY_CLIENT_SECRET
        }
    )

    token_info = response.json()

    session['access_token'] = token_info['access_token']
    session['refresh_token'] = token_info['refresh_token']
    session['expires_at'] = datetime.datetime.now().timestamp() + token_info['expires_in']

    return redirect(url_for('auth.create_user'))


@auth_bp.route('/create-user')
def create_user():
    if 'access_token' not in session:
        return redirect(url_for('auth.login'))

    headers = {
        'Authorization': f"Bearer {session['access_token']}"
    }

    response = requests.get(API_BASE_URL + 'me', headers=headers)
    user_info = response.json()

    spotify_id = user_info['id']

    profile_col.update_one(
        {"spotify_id": spotify_id},
        {"$set": {
            "name": user_info.get("display_name"),
            "profilepic": user_info["images"][0]["url"] if user_info.get("images") else None,
            "spotify": {
                "access_token": session["access_token"],
                "refresh_token": session["refresh_token"],
                "expires_at": session["expires_at"]
            }
        }},
        upsert=True
    )

    # 🔐 Create YOUR app JWT
    jwt_token = create_access_token(
        identity=spotify_id,
        expires_delta=datetime.timedelta(days=7)
    )

    response = make_response(redirect(f'{FRONTEND_URL}'))  # 👈 your app page
    response.set_cookie(
        "access_token_cookie",
        jwt_token,
        httponly=True,
        secure=False,
        samesite="Lax"
    )

    return response


@auth_bp.route('/refresh-tokens')
def refresh_token():
    if 'refresh_token' not in session:
        return redirect(url_for('auth.login'))

    response = requests.post(
        TOKEN_URL,
        data={
            'grant_type': 'refresh_token',
            'refresh_token': session['refresh_token'],
            'client_id': SPOTIFY_CLIENT_ID,
            'client_secret': SPOTIFY_CLIENT_SECRET
        }
    )

    token_info = response.json()

    session['access_token'] = token_info['access_token']
    session['expires_at'] = datetime.datetime.now().timestamp() + token_info['expires_in']

    return redirect('/dashboard')

@auth_bp.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"success": True})
    response.delete_cookie("access_token_cookie")
    session.clear()
    return response, 200

@auth_bp.route("/me", methods=["GET"])
def me():
    try:
        verify_jwt_in_request()  # reads access_token_cookie automatically
        userid = get_jwt_identity()
        return jsonify({
            "authenticated": True,
            "user_id": userid
        }), 200
    except Exception:
        return jsonify({"authenticated": False}), 401
