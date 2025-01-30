import { defineStore } from 'pinia';
import router from '@/router';
import { useCalendarStore } from './calendarStore';
import { usePatientModalStore } from '@/stores/patientModal';

let activityTimeout = null;

export const useAuthStore = defineStore('auth', {
    state: () => ({
        accessToken: null,
        refreshToken: null,
        user: null,
        error: null, 
        role: null,
    }),
    actions: {
        startInactivityTimer() {
            // Clear any existing timer
            clearTimeout(activityTimeout);

            // Set a new timer for inactivity
            activityTimeout = setTimeout(async () => {
                console.warn("User inactive for too long. Logging out...");
                await this.logout();
            }, 10 * 60 * 1000); 
        },
    
        resetInactivityTimer() {
            this.startInactivityTimer(); 
        },
    
        monitorActivity() {
            //event listeners to reset the timer on user activity
            window.addEventListener("mousemove", this.resetInactivityTimer);
            window.addEventListener("keydown", this.resetInactivityTimer);
            window.addEventListener("click", this.resetInactivityTimer);

            // Start the inactivity timer
            this.startInactivityTimer();
        },

        stopMonitoringActivity() {
            // Remove event listeners and clear the timer
            window.removeEventListener("mousemove", this.resetInactivityTimer);
            window.removeEventListener("keydown", this.resetInactivityTimer);
            window.removeEventListener("click", this.resetInactivityTimer);
            clearTimeout(activityTimeout);
        },

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

                this.monitorActivity();

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

                const calendar = useCalendarStore();
                await calendar.getEvents(data.access_token);

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
                this.stopMonitoringActivity();

                const patientModals = usePatientModalStore();
                patientModals.reset();

                localStorage.removeItem('authAccessToken');
                localStorage.removeItem('authRefreshToken');
                localStorage.removeItem('authRole');
                localStorage.removeItem('authUser');

                router.push({ name: 'sign-in' });
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

        async APICall ({body, api}) {
            try {
                const response = await fetch(`http://127.0.0.1:8000 + ${api}`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        'Authorization': `Bearer ${this.accessToken}`,
                    },
                    body: body,
                });

                if (!response.ok) {
                    const errorData = await response.json();
                    return errorData.error;
                }

                const success = await response.json();
                return success.message;
            } catch (error) {
                return error; 
            }
        },
    },

    getters: {
        isAuthenticated: (state) => !!state.user,
        getUser: (state) => state.user,
        getAccessToken: (state) => state.accessToken,
        getError: (state) => state.error,
        getRole: (state) => state.role,
    },
});