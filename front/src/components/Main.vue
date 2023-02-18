<template>
    <div class="main">
        <div class="main-top">
            <div class="main-tab" 
                    v-for="tab in tabs" 
                    :key="tab.key"
                    @click="changeMode(tab.key)">
                {{ tab.name }}
            </div>
        </div>
        <SearchDistrictRegions v-if="mode === 'search'" @close="close" @open="open" />
        <DistrictList v-if="mode === 'district'" @close="close" />
        <Compare v-if="mode === 'compare'" @close="close" />
    </div>
</template>

<script>
export default {
    data() {
        return {
            tabs: [
                {
                    name: 'Поиск',
                    key: 'search'
                },
                {
                    name: 'Округи регионы',
                    key: 'district'
                },
                {
                    name: 'Сравнение',
                    key: 'compare'
                },
            ],

            mode: null,
            selectedDistrict: null,
        }
    },
    computed: {

    },
    methods: {
        changeMode(mode) {
            this.mode = mode
        },
        close() {
            this.mode = null
        },
        open() {
            this.mode = 'district'
        },
    },
    mounted() {

    },  
}
</script>

<style lang="scss" scoped>
    .main {
        &-top {
            display: flex;
            border-bottom: 1px solid #D2D2D2;
        }

        &-tab {
            padding: 35px 56px;
            font-size: 25px;
            line-height: 30px;
            cursor: pointer;

            &:not(:last-child) {
                border-right: 1px solid #D2D2D2;
            }
        }
    }
</style>
