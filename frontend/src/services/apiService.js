import axios from "axios";
import {baseURL} from "../constants/urls";
import {authService} from "./authService";

const apiService = axios.create({baseURL})

apiService.interceptors.request.use(req => {
    const token = localStorage.getItem('access');

    if (token) {
        req.headers.Authorization = `Bearer ${token}`
    }

    return req
})

apiService.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;

        if (error.response?.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;

            try {
                const refreshToken = localStorage.getItem("refresh");
                if (!refreshToken) {
                    throw new Error("Refresh token missing");
                }

                await authService.refresh(refreshToken);

                return apiService(originalRequest);
            } catch (refreshError) {
                console.error("Failed to refresh token", refreshError);
                window.location.href = "/login";
                return Promise.reject(refreshError);
            }
        }

        return Promise.reject(error);
    }
);

export {
    apiService
}