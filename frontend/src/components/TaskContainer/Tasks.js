import {useEffect, useState} from "react";
import {socketService} from "../../services/socketService";
import {taskService} from "../../services/taskService";
import {Task} from "./Task";

const Tasks = () => {
    const [tasks, setTasks] = useState([])
    const [trigger, setTrigger] = useState(null)

    useEffect(() => {
        taskService.getAll().then(({data}) => setTasks(data.data))
    }, [trigger]);

    useEffect(() => {
        socketInit()
    }, []);

    const socketInit = async () => {
        const {tasks} = await socketService();
        const client = await tasks();

        client.onopen = () => {
            console.log('task socket connected');
            client.send(JSON.stringify({
                action: 'subscribe_to_task_activity',
                request_id: new Date().getTime()
            }))
        }

        client.onmessage = ({data}) => {
            console.log(data);
            setTrigger(prev => !prev)
        }
    }

    return (
        <div>
            {tasks.map(task => <Task key={task.id} task={task}/>)}
        </div>
    );


};

export {Tasks};