import { createRouter, createWebHashHistory } from 'vue-router';
import Chart from '@/components/charts/Chart.vue'

const routes = [
    {
        path: '/',
        name: 'Chart',
        component: Chart,
    }
]

export default createRouter({
    history: createWebHashHistory(),
    routes
})