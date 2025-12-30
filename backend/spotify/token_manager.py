import time
import os
import requests
from db import profile_col

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
TOKEN_URL = "https://accounts.spotify.com/api/token"

def get_valid_spotify_token(spotify_id):
    user = profile_col.find_one({"spotify_id": spotify_id})

    if not user or "spotify" not in user:
        raise Exception("Spotify not connected")

    spotify = user["spotify"]

    # token still valid
    if time.time() < spotify["expires_at"]:
        return spotify["access_token"]

    # refresh token
    response = requests.post(
        TOKEN_URL,
        data={
            "grant_type": "refresh_token",
            "refresh_token": spotify["refresh_token"],
            "client_id": SPOTIFY_CLIENT_ID,
            "client_secret": SPOTIFY_CLIENT_SECRET
        }
    )

    data = response.json()

    new_access_token = data["access_token"]
    expires_at = time.time() + data["expires_in"]

    profile_col.update_one(
        {"spotify_id": spotify_id},
        {"$set": {
            "spotify.access_token": new_access_token,
            "spotify.expires_at": expires_at
        }}
    )

    return new_access_token
