import {useForm} from "react-hook-form";
import {taskService} from "../../services/taskService";

const TaskForm = () => {
    const {register, handleSubmit, reset} = useForm();


    const save = async (task) => {
        await taskService.create(task)
        reset()
    }
    return (
        <form onSubmit={handleSubmit(save)}>
            <input type="text" placeholder={'description'} {...register('description')}/>
            <input type="text" placeholder={'priority'} {...register('priority')}/>
            <button>save</button>
        </form>
    );
};

export {TaskForm};