import {createBrowserRouter, Navigate} from "react-router-dom";
import {MainLayout} from "./layouts/MainLayout";
import {LoginPage} from "./pages/LoginPage";
import {CarPage} from "./pages/CarPage";
import {TaskPage} from "./pages/TaskPage";

const router = createBrowserRouter([
    {
        path: '', element: <MainLayout/>, children: [
            {
                index: true, element: <Navigate to={'login'}/>
            },
            {
                path: 'login', element: <LoginPage/>
            },
            {
                path: 'cars', element: <CarPage/>
            },
            {
                path: 'tasks', element: <TaskPage/>
            }
        ]
    }
])

export {
    router
}