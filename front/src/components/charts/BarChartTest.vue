<template>
    <Bar :data="chartData" :options="chartOptions" ref="chart" class="chart" />
</template>

<script>
import { Bar } from 'vue-chartjs'

export default {
    components: {
        Bar
    },
    data() {
        return {
            chartData: {
                labels: [ 'График', 'График', 'March' ],
                datasets: [ { data: [40, 20, 12] } ]
            },
            chartOptions: {
                responsive: true,
            }
        }
    },
    computed: {
        
    },  
    methods: {
        
    },
}
</script>
