import { createApp } from 'vue'
import '@/style.css'
import App from '@/App.vue'
import store from '@/store'
import router from '@/router'
import api from '@/api'
import utils from '@/utils/components'

const app = createApp(App)
app.use(store);
app.use(router);
app.use(api);
utils(app);
app.mount('#app');
