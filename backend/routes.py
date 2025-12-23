from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from pipeline.playlistContext import PlaylistContext
from container import playlist_pipeline

chat_bp = Blueprint("chat", __name__)

@chat_bp.route('/create', methods=["POST"])
@jwt_required()
def create():
    ctx = PlaylistContext(
        user_id=get_jwt_identity(),
        user_query=request.json.get("query"),
    )

    result_ctx = playlist_pipeline.run(ctx)

    return jsonify(result_ctx.songs)