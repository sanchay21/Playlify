from flask_jwt_extended import get_jwt_identity
from db import profile_col

def get_user_top_artists(user_id):
    user = profile_col.find_one({"spotify_id": user_id})

    if not user or "top_artists" not in user:
        return []

    top_artists = user["top_artists"]

    result = [
        {
            "rank": artist.get("rank"),
            "name": artist.get("name")
        }
        for artist in top_artists
    ]

    return result

def get_top_genres(user_id, limit=5):
    user = profile_col.find_one({"spotify_id": user_id})

    if not user or "genres" not in user:
        return []

    sorted_genres = sorted(
        user["genres"].items(),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        {"genre": genre, "count": count}
        for genre, count in sorted_genres[:limit]
    ]
    
def user_music_preference_builder(user_id, top_genres_limit=5):
    top_artists = get_user_top_artists(user_id)
    top_genres = get_top_genres(user_id, limit=top_genres_limit)

    preference_profile = {
        "music_preferences": {
            "top_artists": top_artists,
            "top_genres": top_genres
        }
    }

    return preference_profile



        
        