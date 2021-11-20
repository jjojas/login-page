import { createRouter, createWebHistory } from 'vue-router'
import LoginFormComponent from "../views/LoginForm.vue"
import SuccessComponent from "../views/Success.vue"

const routes = [
  {
    path: '/',
    name: 'Home',
    component: LoginFormComponent
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginFormComponent
  },
  {
    path: '/success',
    name: 'Success',
    component: SuccessComponent
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
