from flask import Blueprint, jsonify, request, session
from flask_jwt_extended import jwt_required, get_jwt_identity
import requests

API_BASE_URL = 'https://api.spotify.com/v1/'

def createPlaylist(user_id, songs, playName, spotify_token):
    headers = {
        'Authorization':f"Bearer {spotify_token}",
        'Content-Type':"application/json"
    }

    data = {
        "name": playName,
        "public":False,
        "description":"Gen By playlify"
    }

    response = requests.post(API_BASE_URL + f'users/{user_id}/playlists', headers = headers, json=data)
    #response.raise_for_status()
    plalist = response.json()
    return plalist
    