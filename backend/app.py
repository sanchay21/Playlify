import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from dotenv import load_dotenv
# import blueprints
from spotify.auth import auth_bp
from spotify.make_music_profile import profile_bp
from llm.routes import llm_bp
from routes import chat_bp, test_bp

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")  # REQUIRED
app.config["JWT_TOKEN_LOCATION"] = ["cookies", "headers"]
app.config["JWT_COOKIE_CSRF_PROTECT"] = False  # for now
app.config["JWT_BLACKLIST_ENABLED"] = False
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = ["access"]
app.config["JWT_ACCESS_COOKIE_NAME"] = "access_token_cookie"

app.config["JWT_COOKIE_SECURE"] = False   # True only in HTTPS
app.config["JWT_COOKIE_SAMESITE"] = "Lax"
FRONTEND_URL = os.getenv("FRONTEND_URL")

jwt = JWTManager(app)
CORS(app, origins=[FRONTEND_URL], supports_credentials=True,)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(profile_bp, url_prefix="/profile")
app.register_blueprint(llm_bp, url_prefix="/chat")
app.register_blueprint(chat_bp, url_prefix="/playlify")
app.register_blueprint(test_bp, url_prefix="/test")

@app.route('/')
def home():
    return "Welcome to the Flask"

if __name__ == '__main__':
    app.run(debug=True, port=8000)