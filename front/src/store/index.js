import { createStore } from 'vuex'

export default createStore({
    state () {
        return {
            loading: false,
            loadingCount: 0,
        }
    },
    getters: {
        loading(state) {
            return state.loading
        }
    },
    mutations: {
        setLoading(state, value) {
            if (value) {
                state.loadingCount++
            } else {
                state.loadingCount--
            }
            state.loading = state.loadingCount > 0
        }
    },
    actions: {
        setLoading(context, value) {
            context.commit('setLoading', value)
        }
    }
})