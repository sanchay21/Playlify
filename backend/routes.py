from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from pipeline.playlistCreationPipeline import PlaylistPipeline
from container import playlist_pipeline

chat_bp = Blueprint("chat", __name__)

@chat_bp.route('/create', methods=["POST"])
@jwt_required()
def create():
    
    ctx = PlaylistPipeline(
        rate_limiter=playlist_pipeline.rate_limiter,
        intent_classifier=playlist_pipeline.intent_classifier,
        rag_retriever=playlist_pipeline.rag_retriever,
        user_music_prefernces=playlist_pipeline.user_music_prefernces,
        llm_client=playlist_pipeline.llm_client,
        spotify_playlist_creation=playlist_pipeline.spotify_playlist_creation,
        chat_func=playlist_pipeline.chat_func
    )
    ctx.user_id = get_jwt_identity()
    ctx.user_query = request.json.get("query")

    result_ctx = playlist_pipeline.run(ctx)

    return jsonify({"songs": result_ctx.songs})
    