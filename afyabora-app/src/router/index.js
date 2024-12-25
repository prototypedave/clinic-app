// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from '@/views/DashboardView.vue'
import EmployeeView from '@/views/EmployeeView.vue'
import RecordsView from '@/views/RecordView.vue'
import AdminRegistration from '@/views/AdminRegistrationView.vue'
import SignIn from '@/views/SignInView.vue'

const routes = [
  { path: '/admin/dashboard', name: 'Dashboard', component: DashboardView,},
  { path: '/admin/employees', name: 'Employee', component: EmployeeView,},
  { path: '/admin/records', name: 'Record', component: RecordsView,},
  { path: '/@admin/registration', name: 'Admin', component: AdminRegistration,},
  { path: '/sign-in', name: 'SignIn', component: SignIn,},
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
