import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/login',  
    },
    {
      path: '/@admin',
      name: 'admin-reg',
      component: () => import('../views/AdminRegistrationView.vue'),
    },
    {
      path: '/login',
      name: 'sign-in',
      component: () => import('../views/SignInView.vue'),
    },
    {
      path: '/admin/dashboard',
      name: 'admin-home',
      component: () => import('../views/AdminDashboardView.vue'),
    },
    {
      path: '/:catchAll(.*)',
      name: 'not-found',
      component: () => import('../components/errors/PageNotFound.vue'),
    }
  ],
})

export default router
