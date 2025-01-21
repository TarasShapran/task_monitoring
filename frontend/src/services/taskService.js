import {apiService} from "./apiService";
import {urls} from "../constants/urls";

const taskService = {
    getAll() {
        return apiService.get(urls.tasks)
    },
    create(data) {
        return apiService.post(urls.tasks, data)
    }
}

export {
    taskService
}