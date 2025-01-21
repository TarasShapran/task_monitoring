const baseURL = '/api'

const auth = '/auth'
const cars = '/cars'
const tasks = '/tasks'

const urls = {
    auth: {
        login: auth,
        socket: `${auth}/socket`
    },
    cars,
    tasks
}

export {
    baseURL,
    urls
}