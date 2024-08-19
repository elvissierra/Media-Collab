import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

const app = createApp(App)

axios.defaults.baseURL = 'http://localhost:8000/api/'
app.config.globalProperties.$axios = axios

app.use(router)

app.mount('#app')