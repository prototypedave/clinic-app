import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    accessToken: null,
    refreshToken: null,
    user: null,
    error: null, 
    role: null,
  }),
  actions: {
    async login({ email, password }) {
      this.error = null; // Clear previous error

      try {
        const response = await fetch("http://127.0.0.1:8000/users/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ email, password }),
        });

        if (!response.ok) {
          const errorData = await response.json();
          this.error = errorData.error || "Login failed";
          throw new Error(this.error); 
        }

        const data = await response.json();
        this.accessToken = data.access_token;
        this.refreshToken = data.refresh_token;
        this.role = data.role;

        // Fetch user profile after login
        const userResponse = await fetch("http://127.0.0.1:8000/users/profile", {
          headers: {
            Authorization: `Bearer ${data.access_token}`,
          },
        });

        if (userResponse.ok) {
          const userData = await userResponse.json();
          this.user = userData;
        }

        return true; 
      } catch (error) {
        console.error(error);
        throw error; 
      }
    },
    logout() {
      this.accessToken = null;
      this.refreshToken = null;
      this.user = null;
      this.error = null;
      this.role = null
    },
    async refreshAccessToken() {
      try {
        const response = await fetch("http://127.0.0.1:8000/users/refresh", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ refresh_token: this.refreshToken }),
        });

        if (!response.ok) {
          this.error = "Failed to refresh token";
          throw new Error(this.error);
        }

        const data = await response.json();
        this.accessToken = data.access_token;
      } catch (error) {
        console.error("Failed to refresh token:", error);
        this.logout();
      }
    },
    async refreshUserData() {
      try {
        const userResponse = await fetch("http://127.0.0.1:8000/users/profile", {
          headers: {
            Authorization: `Bearer ${this.accessToken}`,
          },
        });

        if (userResponse.ok) {
          const userData = await userResponse.json();
          this.user = userData;
        }

        return true; 
      } catch (error) {
        console.error(error);
        throw error; 
      }
    },
  },
  getters: {
    isAuthenticated: (state) => !!state.accessToken,
    getUser: (state) => state.user,
    getAccessToken: (state) => state.accessToken,
    getError: (state) => state.error,
    getRole: (state) => state.role,
  },
});
