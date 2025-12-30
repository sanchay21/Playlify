import { Navigate } from "react-router-dom";
import { useAuth } from "@/hooks/userAuth";

const ProtectedRoute = ({ children }: { children: JSX.Element }) => {
  const { loading, authenticated } = useAuth();

  if (loading) return null; // or loader
  if (!authenticated) return <Navigate to="/auth" replace />;

  return children;
};

export default ProtectedRoute;
