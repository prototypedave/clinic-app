import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/@admin',
      name: 'admin-reg',
      component: () => import('../views/AdminRegistrationView.vue'),
    }
  ],
})

export default router
