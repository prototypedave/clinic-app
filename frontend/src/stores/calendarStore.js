import { defineStore } from 'pinia';
export const useCalendarStore = defineStore('calender', {
  state: () => ({
    events: null,
    error: null,
  }),
  actions: {
    async getEvents(token) {
      try {
        const response = await fetch("http://127.0.0.1:8000/appointments/get-appointments", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        if (!response.ok) {
          const errorData = await response.json();
          this.error = errorData.error || "Login failed";
          throw new Error(this.error); 
        }

        const data = await response.json();
        this.events = data.events;

        localStorage.setItem('events', data.events);

        return true; 
      } catch (error) {
        console.error(error);
        throw error; 
      }
    },
    initializeEventsState() {
      const events = localStorage.getItem('events');

      if (events) {
        this.events = events;
      }
    },
  },
  getters: {
    getAppointments: (state) => state.events,
  },
});