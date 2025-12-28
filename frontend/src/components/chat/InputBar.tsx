import { useState, useRef, useEffect } from "react";
import { motion } from "framer-motion";
import { Mic, ArrowUp } from "lucide-react";

interface InputBarProps {
  onSend: (message: string) => void;
  value: string;
  onChange: (value: string) => void;
}

const InputBar = ({ onSend, value, onChange }: InputBarProps) => {
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const [isFocused, setIsFocused] = useState(false);

  const adjustHeight = () => {
    const textarea = textareaRef.current;
    if (textarea) {
      textarea.style.height = "auto";
      textarea.style.height = `${Math.min(textarea.scrollHeight, 120)}px`;
    }
  };

  useEffect(() => {
    adjustHeight();
  }, [value]);

  const handleSubmit = () => {
    if (value.trim()) {
      onSend(value.trim());
      onChange("");
      if (textareaRef.current) {
        textareaRef.current.style.height = "auto";
      }
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="fixed bottom-0 left-0 right-0 p-4 pb-safe bg-gradient-to-t from-background via-background to-transparent"
      style={{ paddingBottom: "max(1rem, env(safe-area-inset-bottom))" }}
    >
      <div className="max-w-2xl mx-auto">
        <div
          className={`flex items-end gap-2 p-2 rounded-3xl glass transition-all duration-200 ${
            isFocused ? "glow-subtle border-glass-border/60" : ""
          }`}
        >
          <button
            type="button"
            className="flex-shrink-0 w-10 h-10 rounded-full bg-secondary hover:bg-secondary/80 flex items-center justify-center transition-colors"
            aria-label="Voice input"
          >
            <Mic className="w-5 h-5 text-muted-foreground" />
          </button>

          <textarea
            ref={textareaRef}
            value={value}
            onChange={(e) => onChange(e.target.value)}
            onKeyDown={handleKeyDown}
            onFocus={() => setIsFocused(true)}
            onBlur={() => setIsFocused(false)}
            placeholder="Describe your mood..."
            rows={1}
            className="flex-1 bg-transparent text-foreground placeholder:text-muted-foreground text-[15px] resize-none outline-none py-2.5 px-1 max-h-[120px]"
          />

          <button
            type="button"
            onClick={handleSubmit}
            disabled={!value.trim()}
            className={`flex-shrink-0 w-10 h-10 rounded-full flex items-center justify-center transition-all duration-200 ${
              value.trim()
                ? "bg-foreground text-background glow-button hover:scale-105 active:scale-95"
                : "bg-secondary text-muted-foreground"
            }`}
            aria-label="Send message"
          >
            <ArrowUp className="w-5 h-5" />
          </button>
        </div>
      </div>
    </motion.div>
  );
};

export default InputBar;
