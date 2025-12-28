import { motion } from "framer-motion";
import SuggestionCards from "./SuggestionCards";

interface EmptyStateProps {
  onSelectSuggestion: (prompt: string) => void;
}

const EmptyState = ({ onSelectSuggestion }: EmptyStateProps) => {
  return (
    <div className="flex-1 flex flex-col items-center justify-center px-4">
      <motion.div
        initial={{ opacity: 0, y: -10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.4 }}
        className="text-center mb-8"
      >
        <h1 className="text-2xl md:text-3xl font-semibold text-foreground mb-2">
          What do you want to hear today?
        </h1>
        <p className="text-muted-foreground text-base">
          Let's create a playlist together.
        </p>
      </motion.div>

      <SuggestionCards onSelect={onSelectSuggestion} />
    </div>
  );
};

export default EmptyState;
