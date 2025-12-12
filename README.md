# Playlify
An AI-powered multimodal mood-based playlist generator that allows users to input text, images, or voice. It analyzes the user’s mood/vibe using a custom RAG + LLM (or Gemini API) pipeline, combines it with the user’s Spotify listening history, and automatically creates a personalized Spotify playlist that matches both their current mood and music taste, leveraging robust backend services like Redis caching, rate limiting, intent classification, and observability for reliability and performance.

## Key Features
* <b>Multimodal Input</b> — Understands text, voice, and images
* <b>LLM-Powered Mood Detection</b> — Extracts emotional tone and context
* <b>RAG Pipeline</b>ain understanding and memory retrieval
* <b>Spotify Integration</b> — Fetches taste profile + creates dynamic playlists
* <b>Robust Backend Services</b> — Modular architecture with intent classification, rate limiting, Redis caching, and error handling
* <b>Frontend</b> — Clean React interface for chat and playlist previews
* <b>Observability & Reliability</b> — Logging, monitoring, and fault tolerance

## Tech Stack
* <b>Backend</b>: Python, Flask, LLMs, RAG Pipeline, Redis cache, Rate limiter, Intent classifier
* <b>Frontend</b>: React (Vite)
* <b>APIs</b>: Spotify Web API
* <b>Other Services</b>: Vector DB, Logging & Monitoring, Error Handling
