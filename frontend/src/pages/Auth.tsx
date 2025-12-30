  import AnimatedBackground from '@/components/auth/AnimatedBackground';
import AuthCard from '@/components/auth/AuthCard';

const Auth = () => {
  const handleSpotifyConnect = () => {
    window.location.href = "http://127.0.0.1:8000/auth/login";
  };

  return (
    <div className="h-full w-full flex items-center justify-center relative overflow-hidden">
      <AnimatedBackground />
      <AuthCard onSpotifyConnect={handleSpotifyConnect} />
    </div>
  );
};

export default Auth;
