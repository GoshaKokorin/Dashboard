import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    BarElement,
    CategoryScale,
    LinearScale,
    PointElement,
    ArcElement,
    LineElement,
    RadialLinearScale,
    Filler,
} from 'chart.js'

ChartJS.register(
    CategoryScale, 
    LinearScale, 
    BarElement, 
    Title, 
    Tooltip, 
    Legend, 
    PointElement, 
    ArcElement,
    LineElement,
    RadialLinearScale,
    Filler,
)

export default ChartJS