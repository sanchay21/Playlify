import { useNavigate } from 'react-router-dom';
import AnimatedBackground from '@/components/auth/AnimatedBackground';
import AuthCard from '@/components/auth/AuthCard';

const Auth = () => {
  const navigate = useNavigate();

  const handleSpotifyConnect = () => {
    // TODO: Implement Spotify OAuth flow
    // For now, redirect to main chat after mock delay
    console.log('Spotify OAuth initiated');
    
    // Mock successful auth - in real app, this would be handled by OAuth callback
    setTimeout(() => {
      navigate('/');
    }, 2000);
  };

  return (
    <div className="h-full w-full flex items-center justify-center relative overflow-hidden">
      <AnimatedBackground />
      <AuthCard onSpotifyConnect={handleSpotifyConnect} />
    </div>
  );
};

export default Auth;
