const baseURL = '/api'

const auth = '/auth'
const tasks = '/tasks'

const urls = {
    auth: {
        login: auth,
        refresh: `${auth}/refresh`,
        socket: `${auth}/socket`
    },
    tasks
}

export {
    baseURL,
    urls
}