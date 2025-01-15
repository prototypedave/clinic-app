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
      this.error = null; 

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

        localStorage.setItem('authAccessToken', data.accessToken);
        localStorage.setItem('authRefreshToken', data.refreshToken);
        localStorage.setItem('authRole', data.role);
        localStorage.setItem('authUser', JSON.stringify(this.user));

        return true; 
      } catch (error) {
        console.error(error);
        throw error; 
      }
    },
    async logout() {
      try {
        const response = await fetch('http://127.0.0.1:8000/users/logout', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${this.accessToken}`, 
          },
        });

        if (!response.ok) {
          throw new Error('Error logging out of your account');
        }
        this.accessToken = null;
        this.refreshToken = null;
        this.user = null;
        this.error = null;
        this.role = null;

        localStorage.removeItem('authAccessToken');
        localStorage.removeItem('authRefreshToken');
        localStorage.removeItem('authRole');
        localStorage.removeItem('authUser');

        return true;  
      } catch (error) {
          console.error("Server Error:", error);
      } 
      
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
        await this.logout();
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
    initializeAuthState() {
      const accessToken = localStorage.getItem('authAccessToken');
      const refreshToken = localStorage.getItem('authRefreshToken');
      const role = localStorage.getItem('authRole');
      const user = localStorage.getItem('authUser');

      if (accessToken && refreshToken && role && user) {
        this.accessToken = accessToken;
        this.refreshToken = refreshToken;
        this.role = role;
        this.user = JSON.parse(user); 
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
