import React, { useState } from "react";
import DateTimePicker from 'react-datetime-picker';
import axios from 'axios';
import "../index.css"
import "./css/EditTask.css"

function AddTask() {
    const [task, setTask] = useState(
        {
            name: '',
            description: '',
            dueTime: new Date()
        }
    )
    function handleChange(event) {
        const { name, value } = event.target;
        console.log("handlechange")
        if (name === "taskdescription")
            setTask(
                { name: task.name, description: value }
            );
        else if (name === "taskname")
            setTask(
                { name: value, description: task.description }
            );
    }
    function dateChange(date) {
        setTask({ name: task.name, description: task.description, dueTime: date })
    }
    async function submitTask() {
        try {
            const response = await axios.post('http://localhost:5000/tasks', task, { withCredentials: true })
            console.log("task successfully submitted")
            return response
        }
        catch (error) {
            console.log(error)
            console.log("error while submitting task")
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
                        value={task.dueTime}
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
                        value="Add Task"
                        onClick={submitTask}
                    />
                </div>

            </form>



        </div>


    );


}

export default AddTask;