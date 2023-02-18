const files = import.meta.glob('@/components/*.vue', { eager: true })
const folders = import.meta.glob('@/components/*/*.vue', { eager: true })

export default (app) => {
    Object.keys(files).forEach(file => {
        const config = files[file];
        const name = /\/\w+\.vue/.exec(file)[0].replace(/^\//, '').replace(/\.\w+$/, '')
        app.component(name, config.default || config)
    });

    Object.keys(folders).forEach(file => {
        const config = folders[file];
        const name = /\/\w+\.vue/.exec(file)[0].replace(/^\//, '').replace(/\.\w+$/, '')
        app.component(name, config.default || config)
    });
}