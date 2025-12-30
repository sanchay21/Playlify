from pipeline.playlistCreationPipeline import PlaylistPipeline

from llm.groq_llm import GroqLLM
from llm.routes import chat_func
from intent_classifier.routes import intent_func
from spotify.user_music_data import user_music_preference_builder


playlist_pipeline = PlaylistPipeline(
    user_music_prefernces = user_music_preference_builder,
    llm_client=GroqLLM(),
    chat_func = chat_func,
    rate_limiter = None,
    intent_classifier = intent_func,
    rag_retriever = None,
    spotify_playlist_creation = None,
)


