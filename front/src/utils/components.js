const modules = import.meta.glob('@/components/*.vue', { eager: true })

export default (app) => {
    Object.keys(modules).forEach(file => {
        const config = modules[file];
        const name = /\/\w+\.vue/.exec(file)[0].replace(/^\//, '').replace(/\.\w+$/, '')
        app.component(name, config.default || config)
    });
}