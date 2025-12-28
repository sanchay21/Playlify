import { useRef, useEffect } from "react";
import MessageBubble from "./MessageBubble";

interface Message {
  id: string;
  content: string;
  isUser: boolean;
}

interface MessageListProps {
  messages: Message[];
  isTyping: boolean;
}

const MessageList = ({ messages, isTyping }: MessageListProps) => {
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isTyping]);

  return (
    <div className="flex-1 overflow-y-auto scrollbar-hide px-4 py-4">
      <div className="max-w-2xl mx-auto">
        {messages.map((message) => (
          <MessageBubble
            key={message.id}
            content={message.content}
            isUser={message.isUser}
          />
        ))}
        
        {isTyping && (
          <MessageBubble content="" isUser={false} isTyping />
        )}
        
        <div ref={messagesEndRef} className="h-1" />
      </div>
    </div>
  );
};

export default MessageList;
