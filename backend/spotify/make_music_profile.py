from flask import request, jsonify, Blueprint, session, redirect, url_for
from datetime import datetime
import requests
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from db import profile_col


profile_bp = Blueprint("profile", __name__)

API_BASE_URL = 'https://api.spotify.com/v1/'

@profile_bp.route('/musicprofile')
@jwt_required()
def add_music_taste():
    if 'access_token' not in session:
        return redirect(url_for('auth.login'))
    if datetime.now().timestamp() > session['expires_at']:
        return redirect(url_for('auth.refresh_token'))

    headers = {
        'Authorization': f"Bearer {session['access_token']}",
    }

    response_top_art = requests.get(API_BASE_URL + 'me/top/artists?time_range=medium_term&limit=10', headers=headers)
    user_music_taste = response_top_art.json()

    top_artists = []
    genre_counter = {}

    for rank, artist in enumerate(user_music_taste.get("items", []), start=1):

        # store artist info
        artist_data = {
            "rank": rank,
            "artist_id": artist["id"],
            "name": artist["name"],
            "popularity": artist["popularity"],
            "spotify_url": artist["external_urls"]["spotify"],
            "genres": artist["genres"]
        }

        top_artists.append(artist_data)

        # aggregate genres
        for genre in artist["genres"]:
            genre_counter[genre] = genre_counter.get(genre, 0) + 1

    userid  = get_jwt_identity()
    if userid:
        user = profile_col.find_one(
            {"spotify_id":userid}
        )

        profile_col.update_one(
            {"spotify_id":userid},
            {"$set":{
                "top_artists":top_artists,
                "genres":genre_counter
            }},
            upsert = True
        )

    print("Music Taste Updated")
    return redirect(url_for("profile.me"))

@profile_bp.route('/me')
@jwt_required()
def me():
    userid  = get_jwt_identity()
    if userid:
        user = profile_col.find_one(
            {"spotify_id":userid}
        )
        if user:  
            if (user["top_artists"]):
                user_profile = {
                    "name":user["name"],
                    "top_artists":user["top_artists"],
                    "genres":user["genres"]
                }

                return jsonify(user_profile)
            else:
                print("Creating Music Taste")
                return redirect(url_for("profile.add_music_taste"))
        else:
            print("User Does not exist ")
            return redirect("auth.login")
    else:
        return redirect("auth.login")

@profile_bp.route('/getuserdata')
@jwt_required()
def get_user_spotify_data():
    userid  = get_jwt_identity()

    user = profile_col.find_one({"spotify_id":userid}, {"_id": 0})

    top_artists = sorted(
        [(artist["rank"], artist["name"]) for artist in user["top_artists"]],
        key=lambda x: x[0]
    )
    print(top_artists)
    return jsonify(user) 

    