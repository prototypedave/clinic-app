import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import { useTokenStore } from '@/stores/resetToken';
import axios from 'axios';

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
    },
    {
      path: '/reset/password',
      name: 'reser-password',
      component: () => import('../views/ResetPasswordView.vue'),
    },
    {
      path: '/change-password/:token',
      name: 'new-password',
      component: () => import('../views/ChangePasswordView.vue'),
      beforeEnter: async (to, from, next) => {
        try {
          const response = await axios.get(`http://localhost:8000/users/validate-token/${to.params.token}`);

          if (response.data.valid) {
            const tokenStore = useTokenStore();
            tokenStore.saveResetToken(to.params.token);
            next();
          } else {
            next({ name: 'not-found' }); 
          }
        } catch (error) {
          // Handle backend errors (expired or invalid token)
          if (error.response && error.response.status === 400) {
            console.warn('Token expired or invalid:', error.response.data.error);
            const tokenStore = useTokenStore();
            tokenStore.clearResetToken(); // Clear frontend token
            next({ name: 'home' }); // Redirect to home
          } else {
            console.error('Unexpected error:', error);
            next({ name: 'home' }); // Redirect to home on unexpected errors
          }
        }
      },
    },
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
