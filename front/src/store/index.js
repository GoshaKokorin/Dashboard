import { createStore } from 'vuex'

export default createStore({
    state () {
        return {
            loading: false,
            loadingCount: 0,
            selectedDistrict: null,
            selectedRegion: null,
            districts: [
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
    getters: {
        loading(state) {
            return state.loading
        },
        selectedDistrict(state) {
            return state.selectedDistrict
        },
        selectedRegion(state) {
            return state.selectedRegion
        },
    },
    mutations: {
        setLoading(state, value) {
            if (value) {
                state.loadingCount++
            } else {
                state.loadingCount--
            }
            state.loading = state.loadingCount > 0
        },
        setSelectedDistrict(state, value) {
            state.selectedDistrict = value
        },
        setSelectedRegion(state, value) {
            state.selectedRegion = value
        },
    },
    actions: {
        setLoading(context, value) {
            context.commit('setLoading', value)
        },
        setSelectedItem({ commit, state }, value) {
            if (value.isRegion) {
                let parent = state.districts.find(x => x.id === value.parent)
                commit('setSelectedDistrict', parent)
                commit('setSelectedRegion', value)
            } else {
                commit('setSelectedDistrict', value)
            }
        }
    }
})