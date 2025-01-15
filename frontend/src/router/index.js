import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
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
      meta: { requiresAuth: true, role: 'admin' },
    },
    {
      path: '/:catchAll(.*)',
      name: 'not-found',
      component: () => import('../components/errors/PageNotFound.vue'),
    }
  ],
})


router.beforeEach((to, from, next) => {
  const authStore = useAuthStore(); 
  const isAuthenticated = !!authStore.isAuthenticated; 

  if (to.meta.requiresAuth) {
    if (!isAuthenticated) {
      return next({ name: 'sign-in' });
    }

    if (to.meta.role && authStore.getRole !== to.meta.role) {
      return next({ name: 'not-found' }); 
    }
  }

  next(); 
});

export default router
