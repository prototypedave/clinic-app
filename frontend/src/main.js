import './index.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import { useAuthStore } from '@/stores/auth';
import { useCalendarStore } from '@/stores/calendarStore';

const app = createApp(App)

app.use(createPinia())
app.use(router)

const authStore = useAuthStore();
authStore.initializeAuthState();

const calendarStore = useCalendarStore();
calendarStore.initializeEventsState();

app.mount('#app')
