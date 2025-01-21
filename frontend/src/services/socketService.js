import {authService} from "./authService";
import {w3cwebsocket as W3cwebsocket} from 'websocket'

const baseURL = 'ws://localhost/api'

const socketService = async () => {
    const {data: {token}} = await authService.getSocketToken();
    return {
        chat: (room) => new W3cwebsocket(`${baseURL}/chat/${room}/?token=${token}`),
        cars: () => new W3cwebsocket(`${baseURL}/cars/?token=${token}`),
        tasks: () => new W3cwebsocket(`${baseURL}/tasks/?token=${token}`)
    }
}

export {
    socketService
}