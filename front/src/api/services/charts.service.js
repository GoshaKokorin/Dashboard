const funcApi = api => {
    api.charts = {
        getCharts(url) {
            return api.request.get('/api/hello');
        },
    }
}

export default funcApi;