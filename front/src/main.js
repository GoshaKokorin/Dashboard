import { createApp } from 'vue'
import '@/style.css'
import '@/assets/font/stylesheet.css'
import App from '@/App.vue'
import store from '@/store'
import router from '@/router'
import api from '@/api'
import utils from '@/utils/components'
import chartJS from '@/utils/chart-register'

const app = createApp(App)
app.use(store);
app.use(router);
app.use(api);
utils(app);
app.mount('#app');
