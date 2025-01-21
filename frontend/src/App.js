import {useEffect, useState} from "react";
import axios from "axios";

const App = () => {
    const [tasks, setTasks] = useState([])

    useEffect(() => {
        axios.get('/api/tasks').then(({data}) => {
            setTasks(data)
        })
    }, []);

    return (
        <div>
            <h1>Tasks</h1>
            {tasks.map(task=><div key={task.id}>{JSON.stringify(task)}</div>)}
        </div>
    );
};

export {App};