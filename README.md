# Playlify
An AI-powered multimodal mood-based playlist generator that allows users to input text, images, or voice. It analyzes the user’s mood/vibe using a custom RAG + LLM (or Gemini API) pipeline, combines it with the user’s Spotify listening history, and automatically creates a personalized Spotify playlist that matches both their current mood and music taste, leveraging robust backend services like Redis caching, rate limiting, intent classification, and observability for reliability and performance.

## Key Features
* Multimodal Input — Understands text, voice, and images
* LLM-Powered Mood Detection — Extracts emotional tone and context
* RAG Pipeline — Adds domain understanding and memory retrieval
* Spotify Integration — Fetches taste profile + creates dynamic playlists
* Robust Backend Services — Modular architecture with intent classification, rate limiting, Redis caching, and error handling
* Frontend — Clean React interface for chat and playlist previews
* Observability & Reliability — Logging, monitoring, and fault tolerance

## Tech Stack
* Backend: Python, Flask, LLMs, RAG Pipeline, Redis cache, Rate limiter, Intent classifier
* Frontend: React (Vite)
* APIs: Spotify Web API
* Other Services: Vector DB, Logging & Monitoring, Error Handling
