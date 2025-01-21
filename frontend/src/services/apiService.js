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

        if (!originalRequest._retry) {
            originalRequest._retry = true;
            originalRequest._retryCount = 0;
        }
        const MAX_RETRY_COUNT = 3;

        if (error.response?.status === 401 && originalRequest._retryCount < MAX_RETRY_COUNT) {
            originalRequest._retryCount += 1;

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

        if (originalRequest._retryCount >= MAX_RETRY_COUNT) {
            console.warn("Max retry attempts reached");
            window.location.href = "/login";
        }

        return Promise.reject(error);
    }
);

export {
    apiService
}