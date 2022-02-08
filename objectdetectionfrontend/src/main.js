import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import BootstrapVue3 from 'bootstrap-vue-3'
// import BootstrapIcons from 'bootstrap-icons'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'

import '@/css//body.css'
import '@/css/app.css'
import '@/css/Home_css/navbar.css'
import '@/css/Project_css/project.css'

createApp(App).use(store).use(router).use(BootstrapVue3).mount('#app')
