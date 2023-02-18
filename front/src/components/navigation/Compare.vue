<template>
    <Modal @close="$emit('close')">
        <div class="compare">
            <div class="compare-title">Сравнение</div>
        </div>
    </Modal>
</template>

<script>
export default {
    data() {
        return {

        }
    },
    computed: {

    },
    methods: {

    },
    mounted() {

    },  
}
</script>

<style lang="scss" scoped>
    .compare {
        padding: 56px;
        background: #fff;
        width: 390px;
        height: 100%;
        box-sizing: border-box;

        &-title {
            font-size: 32px;
            line-height: 38px;
        }
    }
</style>
