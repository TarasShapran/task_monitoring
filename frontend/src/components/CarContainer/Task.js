const Task = ({task}) => {
    const {id, description, priority, status, user} = task;
    return (
        <div>
            <div>id: {id}</div>
            <div>description: {description}</div>
            <div>priority: {priority}</div>
            <div>status: {status}</div>
            <div>user: {user ? user.email : 'Not assigned'}</div>
        </div>
    );
};

export {Task};