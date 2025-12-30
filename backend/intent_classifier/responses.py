import random

GENERIC_RESPONSES = {
    "GREETING": [
        "Hey! 🎶 Tell me your mood and I'll create a playlist for you.",
        "Hi there! What kind of music are you in the mood for today?",
        "Yo! 😄 Drop a vibe and I'll make a playlist."
    ],

    "THANKS": [
        "You're welcome! 🎧 Enjoy the music.",
        "Anytime! Let me know if you want another playlist.",
        "Glad you liked it! 🔥"
    ],

    "GOODBYE": [
        "See you! Come back when you need more music 🎵",
        "Bye! Hope the playlist keeps you vibing 🎶",
        "Catch you later 👋"
    ],

    "OTHER": [
        "🎵 Want me to create a playlist? Just tell me your mood or vibe.",
        "I can make playlists for any mood, genre, or moment!",
        "Not sure what you mean 😅 — want a playlist?"
    ]
}

def generic_responses(intent: str) -> str:
    responses = GENERIC_RESPONSES.get(intent, GENERIC_RESPONSES["OTHER"])
    return random.choice(responses)