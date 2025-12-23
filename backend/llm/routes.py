from flask import Blueprint, jsonify, request
from llm.groq_llm import GroqLLM, getLLM
import json

llm_bp = Blueprint("llm", __name__)

def chat_func(query, preferences):
    llm = getLLM()
    user_prompt = f"""
You are an AI DJ and music recommendation engine. Your goal is to create a playlist tailored to a user's query and music preferences.

User Query: {query}
User Music Preferences: {preferences}

The user query may describe one or more of the following:
- Their current mood (e.g., happy, sad, energetic)
- The vibe or atmosphere they want (e.g., chill, party, romantic)
- A reference to another playlist or song (e.g., "generate me a playlist like...")

Instructions:
1. Generate a list of exactly 10 songs.
2. **Return only the song titles** as a VALID JSON object in the following format ONLY:
["Song 1", "Song 2", ..., "Song 10"]
3. Do NOT include artist names, explanations, commentary, or markdown formatting.
4. Output must be strictly like: ["Song 1", "Song 2", ..., "Song 10"]
5. Focus on matching the user's preferred genres and mood from the query.

Return the JSON array only.
"""


    response = llm.generate(prompt=user_prompt)
    parsed = json.loads(response)

    return {
        "songs":parsed
    }