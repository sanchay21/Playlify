import { motion } from "framer-motion";
import { CloudRain, Brain, Car, Moon } from "lucide-react";

interface SuggestionCardsProps {
  onSelect: (prompt: string) => void;
}

const suggestions = [
  {
    icon: CloudRain,
    prompt: "Create a playlist for a rainy night",
    gradient: "from-blue-500/20 to-purple-500/20",
  },
  {
    icon: Brain,
    prompt: "Songs for deep focus",
    gradient: "from-emerald-500/20 to-teal-500/20",
  },
  {
    icon: Car,
    prompt: "Happy vibes for a long drive",
    gradient: "from-amber-500/20 to-orange-500/20",
  },
  {
    icon: Moon,
    prompt: "Late-night chill music",
    gradient: "from-indigo-500/20 to-violet-500/20",
  },
];

const SuggestionCards = ({ onSelect }: SuggestionCardsProps) => {
  return (
    <div className="w-full overflow-x-auto scrollbar-hide pb-4 md:flex md:justify-center">
      <div className="flex gap-3 px-4 min-w-max md:min-w-0 md:flex-wrap md:justify-center md:max-w-3xl">
        {suggestions.map((suggestion, index) => (
          <motion.button
            key={suggestion.prompt}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 * index, duration: 0.3 }}
            onClick={() => onSelect(suggestion.prompt)}
            className={`flex flex-col items-start gap-3 p-4 rounded-2xl bg-gradient-to-br ${suggestion.gradient} border border-glass-border backdrop-blur-sm min-w-[160px] max-w-[180px] hover:scale-[1.02] active:scale-[0.98] transition-transform`}
          >
            <div className="w-10 h-10 rounded-xl bg-secondary/50 flex items-center justify-center">
              <suggestion.icon className="w-5 h-5 text-foreground/80" />
            </div>
            <p className="text-sm text-foreground/90 text-left leading-snug">
              {suggestion.prompt}
            </p>
          </motion.button>
        ))}
      </div>
    </div>
  );
};

export default SuggestionCards;
