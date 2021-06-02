import React, { useState } from "react";
import { useLocation } from 'react-router-dom';
import DateTimePicker from 'react-datetime-picker';
import axios from 'axios';
import "../index.css"
import "./css/EditTask.css"

function EditTask() {
    let location = useLocation();
    console.log(location.state)
    const [task, setTask] = useState(
        {
            name: location.state.data.name,
            description: location.state.data.description,
            dueTime: location.state.data.dueTime,
            _id: location.state.data._id
        }
    )
    
    function handleChange(event) {
        const { name, value } = event.target;
        console.log("handlechange")
        if (name === "taskdescription")
            setTask(
                { name: task.name, description: value, dueTime: task.dueTime, _id: task._id}
            );
        else if (name === "taskname")
            setTask(
                { name: value, description: task.description, dueTime: task.dueTime, _id: task._id }
            );
    }
    function dateChange(date) {
        setTask({ name: task.name, description: task.description, dueTime: date, _id: task._id })
    }
    async function submitTask() {
        try {
            const response = await axios.patch('http://localhost:5000/tasks', task, { withCredentials: true })
            console.log("task successfully edited")
            return response
        }
        catch (error) {
            console.log(error)
            console.log("error while editing task")
            return false
        }
    }
    return (
        <div className="col-md-3">
            <form>
                <div className="dt">
                    <DateTimePicker
                        name="dt"
                        amPmAriaLabel="Select AM/PM"
                        calendarAriaLabel="Toggle calendar"
                        clearAriaLabel="Clear value"
                        dayAriaLabel="Day"
                        hourAriaLabel="Hour"
                        maxDetail="minute"
                        minuteAriaLabel="Minute"
                        monthAriaLabel="Month"
                        nativeInputAriaLabel="Date and time"
                        onChange={dateChange}
                        secondAriaLabel="Second"
                        value={new Date(task.dueTime)}
                        yearAriaLabel="Year"
                    />
                </div>
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
                        value="Edit Task"
                        onClick={submitTask}
                    />
                </div>

            </form>



        </div>


    );


}

export default EditTask;