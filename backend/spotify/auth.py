import os
from flask import redirect, request, Blueprint, jsonify, session, url_for
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import datetime
import requests
from dotenv import load_dotenv
from db import profile_col

import urllib.parse

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1/'

auth_bp = Blueprint("auth", __name__)

@auth_bp.route('/')
def index():
    return "Welcome to Playlify.<a href='/auth/login'> Login with Spotify></a>"

@auth_bp.route('/login')
def login():
    scope = 'user-top-read playlist-modify-private'

    # Parameters to pass when sending request to spotify
    params = {
        'client_id':SPOTIFY_CLIENT_ID,
        'response_type':'code',
        'scope':scope,
        'redirect_uri': REDIRECT_URI,
        'show_dialog':True
    }

    auth_url = f"{AUTH_URL}?{urllib.parse.urlencode(params)}"

    return redirect(auth_url)


@auth_bp.route('/callback')
def callback():
    if 'error' in request.args:
        return jsonify({"error": request.args['error']})

    if 'code' in request.args:
        req_body = {
            'code':request.args['code'],
            'client_id':SPOTIFY_CLIENT_ID,
            'client_secret':SPOTIFY_CLIENT_SECRET,
            'redirect_uri':REDIRECT_URI,
            'grant_type':'authorization_code',
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.post(TOKEN_URL,data=req_body)
        token_info = response.json()

        session['access_token'] = token_info['access_token']
        session['refresh_token'] = token_info['refresh_token']
        session['expires_at'] = datetime.datetime.now().timestamp() + token_info['expires_in']

        # return redirect(url_for('profile.taste'))
        # return redirect(url_for('profile.profile_creation'))
        return redirect(url_for('auth.profile_creation'))

@auth_bp.route('/music-taste')
def profile_creation():
    if 'access_token' not in session:
        return redirect(url_for('auth.login'))
    if datetime.datetime.now().timestamp() > session['expires_at']:
        return redirect(url_for('auth.refresh_token'))


    headers = {
        'Authorization':f"Bearer {session['access_token']}",
    }

    # response  = requests.get(API_BASE_URL + 'me/top/artists?time_range=medium_term&limit=50', headers=headers)
    # music_taste = response.json()

    response = requests.get(API_BASE_URL + 'me/', headers = headers)
    user_info = response.json()

    display_name = user_info['display_name']
    spotifyID = user_info['id']
    img_url = user_info['images'][0]['url']

    profile_col.update_one(
        {"spotify_id":spotifyID},
        {"$set":{"name":display_name, "profilepic":img_url}},
        upsert = True
    )

    return jsonify(user_info)

@auth_bp.route('/refresh-tokens')
def refresh_token():
    if 'refresh_token' not in session:
        return redirect('/login')

    if datetime.datetime.now().timestamp() > session['expires_at']:

        req_body = {
            'grant-type':'refresh_token',
            'refresh_token': session['refresh_token'],
            'client_id':SPOTIFY_CLIENT_ID,
            'client_secret':SPOTIFY_CLIENT_SECRET,
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.post(TOKEN_URL, data=req_body)
        new_token_info = response.json()

        session['access_token'] = new_token_info['access_token']
        session['expires_at'] = datetime.datetime.now().timestamp() + new_token_info['expires_in']

        return redirect('/taste-profile')
