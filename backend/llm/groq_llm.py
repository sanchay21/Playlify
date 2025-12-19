# llm/groq_llm.py
import os
from groq import Groq

from llm.base import BaseLLM
from llm.config import GROQ_MODEL, TEMPERATURE, MAX_TOKENS


class GroqLLM(BaseLLM):
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS
        )

        return response.choices[0].message.content.strip()
