<template>
    <div class="app">
        <Loading v-if="loading" />
        <div class="app-content">
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    data() {
        return {

        }
    },
    computed: {
        ...mapGetters(['loading']),
    },
    methods: {
        goTo(routeName) {
            this.$router.push({name: routeName})
        }
    },
    mounted() {
        this.goTo('Main')
    },  
}
</script>

<style lang="scss" scoped>
    .app {
        :global(*) {
            font-family: 'SF UI Display';
        }

        ::v-deep button {
            border: 1px solid;
            cursor: pointer;
        }

        ::v-deep input:focus-visible {
            border: none;
            outline: none;
        }

        ::v-deep .-pointer {
            cursor: pointer;
        }
    }
</style>
