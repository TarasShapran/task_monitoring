const baseURL = '/api'

const auth = '/auth'
const tasks = '/tasks'

const urls = {
    auth: {
        login: auth,
        socket: `${auth}/socket`
    },
    tasks
}

export {
    baseURL,
    urls
}