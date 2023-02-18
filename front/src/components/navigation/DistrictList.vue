<template>
    <Modal @close="$emit('close')">
        <div class="district-list-wrapper">
            <div class="district-list">
                <div class="district-list-title">Округ</div>
                <div class="district-list-subtitle">Статистика округов</div>
                <div class="district-list-container">
                    <div class="district-item -pointer" 
                            :class="{'-active': selectedDistrict && selectedDistrict.id === item.id}"
                            v-for="item in districts" 
                            :key="item.id"
                            @click="openItem(item)">
                        {{ item.name }}
                    </div>
                </div>
            </div>
            <div class="district-list" v-if="!!selectedDistrict">
                <div class="district-list-title">Регион</div>
                <div class="district-list-subtitle">Статистика региона</div>
                <div class="district-list-container">
                    <div class="district-item -pointer" 
                            :class="{'-active': selectedRegion && selectedRegion.id === item.id}"
                            v-for="item in regions" 
                            :key="item.id"
                            @click="openItem(item)">
                        {{ item.name }}
                    </div>
                </div>
            </div>
        </div>
    </Modal>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
    props: {
        activeKey: String,
    },
    data() {
        return {
            districts: [
                {
                    id: 1,
                    name: 'Северо-Западный',
                },
                {
                    id: 2,
                    name: 'Северная Осетия — Алания',
                }
            ],
            regions: [
                {
                    id: 3,
                    name: 'Белгородская область',
                },
                {
                    id: 4,
                    name: 'Брянская область',
                }
            ],
            active: null,
        }
    },
    computed: {
        ...mapGetters(['selectedDistrict', 'selectedRegion']),
    },
    methods: {
        ...mapActions(['setSelectedItem']),
        openItem(value) {
            this.setSelectedItem(value)
        },
    },
    mounted() {
        if (this.activeKey) {
            this.active = this.activeKey
        }
    },  
}
</script>

<style lang="scss" scoped>
    .district-list {
        padding: 56px;
        background: #fff;
        width: 390px;
        height: 100%;
        box-sizing: border-box;

        &-title {
            font-size: 32px;
            line-height: 38px;
        }

        &-subtitle {
            margin-top: 12px;
            font-size: 20px;
            line-height: 24px;
            color: #929292;
        }

        &-container {
            margin-top: 36px;
        }

        .district-item {
            font-size: 24px;
            line-height: 29px;
            color: #929292;

            &:not(:last-child) {
                margin-bottom: 16px;
            }

            &:hover {
                color: #424242;
            }

            &.-active {
                color: #4098FF;
            }
        }
    }

    .district-list-wrapper {
        display: flex;
        height: 100%;

        & > :last-child:not(:first-child) {
            border-left: 1px solid #D2D2D2;
        }
    }
</style>
