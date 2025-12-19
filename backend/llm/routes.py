from flask import Blueprint, jsonify, request
from llm.groq_llm import GroqLLM

llm_bp = Blueprint("llm", __name__)

@llm_bp.route("/text", methods=["POST"])
def chat_func():
    query = request.json["query"]
    llm = getLLM()
    response = llm.generate(prompt = query)
    return jsonify({"reponse":response})
    
def getLLM():
    # Getting Configured LLM
    return GroqLLM()