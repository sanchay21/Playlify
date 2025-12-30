from flask import Blueprint, jsonify, request, session
from flask_jwt_extended import jwt_required, get_jwt_identity

from pipeline.playlistContext import PlaylistContext
from container import playlist_pipeline
from spotify.create_playlist import createPlaylist
from spotify.token_manager import get_valid_spotify_token

chat_bp = Blueprint("chat", __name__)
test_bp = Blueprint("test", __name__)

@chat_bp.route('/create', methods=["POST"])
@jwt_required()
def create():
    print("RAW JSON:", request.json)
    print("HEADERS:", request.headers)
    ctx = PlaylistContext(
        user_id=get_jwt_identity(),
        user_query=request.json.get("query"),
    )

    result_ctx = playlist_pipeline.run(ctx)

    return jsonify(result_ctx)


@test_bp.route('/create-playlist', methods=['POST'])
@jwt_required()
def create_playlist():
    user_id = get_jwt_identity()
    spotify_token = get_valid_spotify_token(user_id)
    playlist = createPlaylist(user_id=user_id, songs=[], playName="Test Playlist 🎧", spotify_token=spotify_token)

    return jsonify(playlist)