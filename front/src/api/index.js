import axios from "axios";
// const PATH = "http://localhost:8080";

const modules = import.meta.glob('./services/*.service.js', { eager: true })

// axios.defaults.baseURL = PATH;

class API {
    request = axios.create({
        transformRequest: [(data, headers) => {
            this.appVue.$store.dispatch('setLoading', true)
            return data;
        }],
        transformResponse: [(data, headers) => {
            this.appVue.$store.dispatch('setLoading', false)
            try {
                return JSON.parse(data);
            } catch(e) {
                return null
            }
        }],
    });

    constructor() {
        this.request.interceptors.response.use(
            function (response) {
                return response.data;
            },
            function (error) {
                return Promise.reject(error);
            }
        );

        Object.keys(modules).forEach(file => {
            modules[file].default(this)
        });
    }

    install(app) {
		app.config.globalProperties.api = this
        this.appVue = app.config.globalProperties
	}
}

export default new API()