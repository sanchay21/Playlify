import { useState, useCallback } from "react";
import ChatHeader from "./ChatHeader";
import EmptyState from "./EmptyState";
import MessageList from "./MessageList";
import InputBar from "./InputBar";

import { sendTextMessage } from "./api.ts";

interface Message {
  id: string; 
  content: string;
  isUser: boolean;
}

const ChatPage = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputValue, setInputValue] = useState("");
  const [isTyping, setIsTyping] = useState(false);

  const generateId = () => Math.random().toString(36).substring(7);

  const handleSend = useCallback(async (content: string) => {
    if (!content.trim()) return;

    const userMessage: Message = {
      id: generateId(),
      content,
      isUser: true,
    };

    setMessages(prev => [...prev, userMessage]);
    setInputValue("");
    setIsTyping(true);

    try {
      const res = await sendTextMessage(content);

      const aiMessage: Message = {
        id: generateId(),
        content: res.text || "🤖 No response received.",
        isUser: false,
      };

      setMessages(prev => [...prev, aiMessage]);
    } catch (error) {
      console.error(error);

      setMessages(prev => [
        ...prev,
        {
          id: generateId(),
          content: "⚠️ Something went wrong. Please try again.",
          isUser: false,
        },
      ]);
    } finally {
      setIsTyping(false);
    }
  }, []);

  const handleSuggestionSelect = (prompt: string) => {
    setInputValue(prompt);
  };

  const hasMessages = messages.length > 0;

  return (
    <div className="h-full flex flex-col bg-background">
      <ChatHeader />

      {hasMessages ? (
        <MessageList messages={messages} isTyping={isTyping} />
      ) : (
        <EmptyState onSelectSuggestion={handleSuggestionSelect} />
      )}

      <div className="h-24" /> {/* Spacer for input bar */}

      <InputBar
        value={inputValue}
        onChange={setInputValue}
        onSend={handleSend}
      />
    </div>
  );
};

export default ChatPage;
