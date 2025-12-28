import { motion } from "framer-motion";
import { Music } from "lucide-react";

interface MessageBubbleProps {
  content: string;
  isUser: boolean;
  isTyping?: boolean;
}

const MessageBubble = ({ content, isUser, isTyping }: MessageBubbleProps) => {
  return (
    <motion.div
      initial={{ opacity: 0, y: 10, scale: 0.98 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      transition={{ duration: 0.2, ease: "easeOut" }}
      className={`flex ${isUser ? "justify-end" : "justify-start"} mb-3`}
    >
      <div className={`flex items-end gap-2 max-w-[85%] ${isUser ? "flex-row-reverse" : "flex-row"}`}>
        {!isUser && (
          <div className="w-7 h-7 rounded-full bg-primary/20 flex items-center justify-center flex-shrink-0 mb-1">
            <Music className="w-3.5 h-3.5 text-primary" />
          </div>
        )}
        
        <div
          className={`px-4 py-2.5 rounded-2xl ${
            isUser
              ? "bg-user-bubble text-foreground rounded-br-md"
              : "bg-ai-bubble text-foreground rounded-bl-md"
          }`}
        >
          {isTyping ? (
            <div className="flex items-center gap-1 py-1 px-2">
              <span className="w-2 h-2 bg-muted-foreground rounded-full animate-pulse-dot" style={{ animationDelay: "0ms" }} />
              <span className="w-2 h-2 bg-muted-foreground rounded-full animate-pulse-dot" style={{ animationDelay: "200ms" }} />
              <span className="w-2 h-2 bg-muted-foreground rounded-full animate-pulse-dot" style={{ animationDelay: "400ms" }} />
            </div>
          ) : (
            <p className="text-[15px] leading-relaxed whitespace-pre-wrap">{content}</p>
          )}
        </div>
      </div>
    </motion.div>
  );
};

export default MessageBubble;
