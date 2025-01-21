import {apiService} from "./apiService";
import {urls} from "../constants/urls";

const authService = {
    async login(user) {
        try {
            const {data: {access, refresh}} = await apiService.post(urls.auth.login, user);
            localStorage.setItem('access', access);
            localStorage.setItem('refresh', refresh);
        } catch (error) {
            console.error("Login failed:", error);
            throw error; // Повідомлення про помилку для відображення на UI
        }
    },
    async logout() {
        localStorage.removeItem("access");
        localStorage.removeItem("refresh");
        window.location.href = "/login";
    },

    async refresh(refreshToken) {
        const {data: {access, refresh}} = await apiService.post(urls.auth.refresh, { refresh: refreshToken });
        localStorage.setItem('access', access)
        localStorage.setItem('refresh', refresh)
    },
    getSocketToken() {
        return apiService.get(urls.auth.socket)
    }
}

export {
    authService
}