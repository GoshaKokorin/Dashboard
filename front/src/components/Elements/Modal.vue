<template>
    <div class="modal">
        <div class="modal-content">
            <div class="modal-content-slot">
                <slot></slot>
            </div>
            <div class="modal-img-wrapper">
                <Img
                    @click="$emit('close')"
                    class="modal-img"
                    :width="36"
                    :height="36"
                    url="close"
                />
            </div>
        </div>
    </div>
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
    .modal {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100%;
        min-height: 100vh;
        z-index: 1;
        background: rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(5px);

        &-content {
            display: flex;
            height: 100%;
        }

        &-content-slot {
            border-right: 1px solid #D2D2D2;
        }

        &-img {
            cursor: pointer;
        }

        &-img-wrapper {
            width: 100px;
            height: 100px;
            background: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            border-right: 1px solid #D2D2D2;
            border-bottom: 1px solid #D2D2D2;
        }
    }
</style>
