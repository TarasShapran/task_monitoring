import {TaskForm} from "../components/TaskContainer/TaskForm";
import {Tasks} from "../components/TaskContainer/Tasks";
import {Chat} from "../components/TaskContainer/Chat";

const TaskPage = () => {
    return (
        <div>
            <TaskForm/>
            <hr/>
            <Tasks/>
            <Chat/>
        </div>
    );
};

export {TaskPage};