import axios from "axios";
// const PATH = "http://localhost:8080";

const modules = import.meta.glob('./services/*.service.js', { eager: true })

// axios.defaults.baseURL = PATH;

class API {
    request = axios.create();

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
	}
}

export default new API()