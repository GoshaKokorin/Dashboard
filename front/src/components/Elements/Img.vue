<template>
    <div class="img-wrapper" :style="style">
        <img :src="fullUrl" />
    </div>
</template>

<script>
export default {
    props: {
        width: {
            type: Number,
            default: 24
        },
        height: {
            type: Number,
            default: 24
        },
        url: String,
    },
    data() {
        return {

        }
    },
    computed: {
        fullUrl() {
            return `src/assets/icons/${this.url}.png`
        },
        style() {
            return {
                width: this.width + 'px',
                height: this.height + 'px'
            }
        }
    },
    methods: {

    },
    mounted() {

    },  
}
</script>

<style lang="scss" scoped>

</style>
