import { motion } from "framer-motion";
import { Music2, Menu } from "lucide-react";

const ChatHeader = () => {
  return (
    <motion.header
      initial={{ opacity: 0, y: -10 }}
      animate={{ opacity: 1, y: 0 }}
      className="flex items-center justify-between px-4 py-3 border-b border-border/50"
    >
      <button
        type="button"
        className="w-10 h-10 rounded-xl hover:bg-secondary/50 flex items-center justify-center transition-colors"
        aria-label="Menu"
      >
        <Menu className="w-5 h-5 text-muted-foreground" />
      </button>

      <div className="flex items-center gap-2">
        <div className="w-8 h-8 rounded-xl bg-primary/20 flex items-center justify-center">
          <Music2 className="w-4 h-4 text-primary" />
        </div>
        <span className="font-semibold text-foreground">Playlify</span>
      </div>

      <div className="w-10 h-10" /> {/* Spacer for centering */}
    </motion.header>
  );
};

export default ChatHeader;
