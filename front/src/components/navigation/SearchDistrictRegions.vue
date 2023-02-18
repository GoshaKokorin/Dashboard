<template>
    <Modal @close="$emit('close')">
        <div class="search-district">
            <div class="search-district-title">Поиск</div>
            <div class="input-search">
                <Img url="search" />
                <input 
                    v-model="search"
                    @input="onSearch"
                    placeholder="Введите регион или округ"
                />
                <Img v-if="!!search" url="clear-ring" @click="reset" class="-pointer" />
            </div>
            <div v-if="isEmpty" class="search-district-empty">
                Ничего не найдено
            </div>
            <div class="search-district-list" v-if="!!search">
                <div class="search-item -pointer" 
                        v-for="item in checkedItems" 
                        :key="item.id"
                        @click="openItem(item)">
                    {{ item.name }}
                </div>
            </div>
        </div>
    </Modal>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    data() {
        return {
            search: null,
            data: [
                {
                    id: 1,
                    name: 'Северо-Западный',
                },
                {
                    id: 2,
                    name: 'Северная Осетия — Алания',
                },
                {
                    id: 3,
                    isRegion: true,
                    parent: 1,
                    name: 'Белгородская область',
                },
                {
                    id: 4,
                    isRegion: true,
                    parent: 1,
                    name: 'Брянская область',
                }
            ],
        }
    },
    computed: {
        isEmpty() {
            return !(this.checkedItems && this.checkedItems.length) && this.search 
        },
        checkedItems() {
            if (this.search) {
                let search = this.search.toLocaleLowerCase()
                return this.data.filter(x => x.name.toLocaleLowerCase().includes(search))
            } else {
                return []
            }
        }
    },
    methods: {
        ...mapActions(['setSelectedItem']),
        reset() {
            this.search = null
        },
        onSearch() {

        },
        openItem(value) {
            this.$emit('open')
            this.setSelectedItem(value)
        }
    },
    mounted() {

    },  
}
</script>

<style lang="scss" scoped>
    .search-district {
        padding: 56px;
        background: #fff;
        width: 390px;
        height: 100%;
        box-sizing: border-box;

        &-title {
            font-size: 32px;
            line-height: 38px;
            margin-bottom: 36px;
        }

        .input-search {
            display: flex;
            border-bottom: 1px solid #D2D2D2;
            padding: 16px 0;

            input {
                border: none;
                padding-left: 12px;
                width: 100%;
                font-size: 20px;
                line-height: 24px;
            }
        }

        &-empty {
            font-size: 24px;
            line-height: 29px;
            color: #929292;
            margin-top: 36px;
        }

        &-list {
            margin-top: 36px;
        }

        .search-item {
            font-size: 24px;
            line-height: 29px;
            color: #929292;

            &:not(:last-child) {
                margin-bottom: 16px;
            }

            &:hover {
                color: #424242;
            }
        }
    }
</style>
