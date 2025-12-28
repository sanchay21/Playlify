import { motion } from 'framer-motion';
import SpotifyButton from './SpotifyButton';

interface AuthCardProps {
  onSpotifyConnect: () => void;
}

const AuthCard = ({ onSpotifyConnect }: AuthCardProps) => {
  return (
    <motion.div
      className="w-full max-w-sm mx-auto px-6"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, ease: 'easeOut' }}
    >
      {/* Logo/Brand */}
      <motion.div
        className="text-center mb-8"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.1, duration: 0.4 }}
      >
        <h1 className="text-2xl font-semibold text-foreground tracking-tight">
          Playlify
        </h1>
      </motion.div>

      {/* Card */}
      <motion.div
        className="glass rounded-2xl p-8 glow-subtle"
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ delay: 0.15, duration: 0.4 }}
      >
        {/* Headline */}
        <motion.h2
          className="text-xl font-medium text-foreground text-center mb-2"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.2, duration: 0.4 }}
        >
          Turn your mood into music.
        </motion.h2>

        {/* Subheadline */}
        <motion.p
          className="text-muted-foreground text-center text-sm mb-8"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.25, duration: 0.4 }}
        >
          Connect Spotify to generate playlists with AI.
        </motion.p>

        {/* Spotify Button */}
        <SpotifyButton onClick={onSpotifyConnect} />

        {/* Footer note */}
        <motion.p
          className="text-muted-foreground/60 text-xs text-center mt-6"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.4, duration: 0.4 }}
        >
        </motion.p>
      </motion.div>

      {/* Powered by */}
      <motion.p
        className="text-muted-foreground/40 text-xs text-center mt-6"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.5, duration: 0.4 }}
      >
      </motion.p>
    </motion.div>
  );
};

export default AuthCard;
