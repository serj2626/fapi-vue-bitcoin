import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import "bootstrap/dist/css/bootstrap.css"
import "bootstrap-vue/dist/bootstrap-vue.css"

const app = createApp(App)
app
    .use(axios)
    .mount('#app')

