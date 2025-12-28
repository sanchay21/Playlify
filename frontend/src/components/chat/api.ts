import axios from "axios";

// Base URLs (adjust if needed)
const TEXT_API_URL = "http://127.0.0.1:8000/playlify/create";
const VOICE_API_URL = "http://127.0.0.1:5000/voice/voice-chat";

export const sendTextMessage = async (message: string) => {
  try {
    const token = localStorage.getItem("access_token");

    const response = await axios.post(
      TEXT_API_URL,
      { query: message },
      {
        headers: {
          Authorization: `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2Njk0MzA3NiwianRpIjoiZTk5ZDU2MTEtNjBmNi00YzNhLWI0NzctOGI0OGMzYjc2MGY5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjJpN3duemV3Nmt3NGUxaWRjdno0N2x1c24iLCJuYmYiOjE3NjY5NDMwNzYsImV4cCI6MTc2NzU0Nzg3Nn0.IAC7FisNO1rPaK1Tj-wt87MVuK-4ij1XrO1_t63rEvE`,
        },
      }
    );

     const songList: string[] = response.data?.songs?.songs || [];

    return {
      text: songList.length
        ? `🎵 Here's a breakup playlist for you:\n\n${songList
            .map((song, idx) => `${idx + 1}. ${song}`)
            .join("\n")}`
        : null,

      raw: response.data, // keep full response for later use
    };
  } catch (error) {
    console.error("Text API error:", error);
    throw error;
  }
};