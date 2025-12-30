from llm.groq_llm import getLLM
import json


def intent_func(query):
    llm = getLLM()
    user_prompt = f"""
You are an intent classifier for a music playlist app.

Classify the user's message into EXACTLY one of the following intents:
- GREETING
- THANKS
- GOODBYE
- PLAYLIST_REQUEST
- OTHER

Rules:
- Greetings, slang greetings, or casual hellos → GREETING
- Thanking or appreciation → THANKS
- Farewells → GOODBYE
- Any request to create, suggest, recommend, or talk about music or playlists → PLAYLIST_REQUEST
- Anything else → OTHER

Respond ONLY in valid JSON like this:
{{"intent": "<INTENT_NAME>"}}

User message:
"{query}"

Return the JSON array only.
"""


    response = llm.generate(prompt=user_prompt)
    parsed = json.loads(response)

    return {
        "intent": parsed["intent"]
    }