import api from "@/api/api";

export const sendTextMessage = async (message: string) => {
  try {
    const response = await api.post(
        "/playlify/create",
        { query: message },   // payload
        { withCredentials: true }  // config
     );

    const songList: string[] = response.data?.songs?.songs || [];
    const responseText = response.data?.response || "";

    return {
      text: songList.length
        ? `🎵 Here's a playlist for you:\n\n${songList
            .map((song, idx) => `${idx + 1}. ${song}`)
            .join("\n")}`
        : responseText,

      raw: response.data,
    };
  } catch (error) {
    console.error("Text API error:", error);
    throw error;
  }
};
