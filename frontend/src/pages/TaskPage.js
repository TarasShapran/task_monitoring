import {TaskForm} from "../components/CarContainer/TaskForm";
import {Tasks} from "../components/CarContainer/Tasks";

const TaskPage = () => {
    return (
        <div>
            <TaskForm/>
            <hr/>
            <Tasks/>
        </div>
    );
};

export {TaskPage};