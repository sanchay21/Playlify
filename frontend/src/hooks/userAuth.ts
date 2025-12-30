import { useEffect, useState } from "react";
import api from "@/api/api";

export const useAuth = () => {
  const [loading, setLoading] = useState(true);
  const [authenticated, setAuthenticated] = useState(false);

  const checkAuth = () => {
    setLoading(true);
    api
      .get("/auth/me")
      .then(() => setAuthenticated(true))
      .catch(() => setAuthenticated(false))
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    checkAuth();
  }, []);

  const logout = async () => {
    await api.post("/auth/logout");
    setAuthenticated(false);
  };

  return { loading, authenticated, logout };
};
