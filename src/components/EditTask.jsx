import React, {useState} from "react";
import "../index.css"
import "./css/EditTask.css"
import axios from 'axios';

function EditTask() {
    const [task, setTask] = useState(
        {
            name: '',
            description: '',
        }
    )
    function handleChange(event) {
        const { name, value } = event.target;
        console.log("handlechange")
        if (name === "taskdescription")
        setTask(
            {name: task.name, description: value}
        );
        else if (name === "taskname")
        setTask(
            {name: value, description: task.description}   
        );
    }
    async function submitTask(){
        try
        {
            const response = await axios.post('http://localhost:5000/tasks', task,{withCredentials: true})
            console.log("task successfully submitted")
            return response
        }
        catch(error)
        {
            console.log(error)
            console.log("error while submitting task")
            return false
        }
    }
    return (
        <div className="col-md-3">
            <form>
            <div className="taskname">
                    <label htmlFor="Task Name">Task Name ‎‏‏‎ ‎‏‏‎ ‎</label>
                    <input
                        type="text"
                        name="taskname"
                        id="taskname"
                        class="tbox"
                        value={task.name}
                        onChange={handleChange}
                        />
            </div>
            <div className="taskdescription">
                <label htmlFor="taskdescription">Task Description ‎‏‏‎‎‏‏‎ ‎‏‏‎ ‎</label>
                <textarea
                    type="text"
                    name="taskdescription"
                    id="taskdescription"
                    class="descriptiontbox"
                    value={task.description}
                    onChange={handleChange} 
                    />
            </div>
            <div className="submitbutton">
                <input 
                    type="button" 
                    class="button" 
                    value="Add Task" 
                    onClick={submitTask} 
                    />
            </div>    
            </form>
        </div>
    );


}

export default EditTask;