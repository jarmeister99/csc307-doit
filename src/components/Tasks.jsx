import React, {useState, useEffect} from "react";
import { useHistory } from "react-router-dom";
import "../index.css"
import "./css/Tasks.css"
import axios from 'axios';


function Tasks() {
    // tasks API not implemented yet but will return JSON in this form for future reference
    // {{id_1, title_1, due_data_1, ...}, {id_2, title_2, due_date_2, ...}, {id_3, title_3, due_data_3, ...}}
    const [tasks, setTasks] = useState([ ]);
        useEffect(() => {
            fetchAll().then( result => {
               if (result)
                  setTasks(result);
             });
    }, [] );
    

    var history = useHistory()
    // Returns a conditional render of the completed status of a task
    function checkDate(date) {
        if (date) {
          return date.substring(0,10);
        } else {
          return;
        }
    }

    async function submitDelete(task) {
        try {
            const response = await axios.delete('http://localhost:5000/tasks', 
                {withCredentials: true, data: {id: task._id}});
            window.location.reload(false);
            return response.data;
         }
         catch (error){
            console.log(error); 
            return false;         
         }
    }
    async function editTask(task) {
        
        console.log(this)
        history.push({pathname: '/edittask', state: {data: task}})
        
    }

    async function submitDeleteAll(task) {
        try {
            const response = await axios.delete('http://localhost:5000/tasks', 
                {withCredentials: true, data: {delete_all: true}});
            window.location.reload(false);
            return response.data;
         }
         catch (error){
            console.log(error); 
            return false;         
         }
    }

    async function fetchAll() {
        try {
           const response = await axios.get('http://localhost:5000/tasks', {
               withCredentials: true});
           return response.data;
        }
        catch (error){
           console.log(error); 
           return false;         
        }
     }

    return (
        <div className="container">
            <h3 className="p-3 text-center">DO-IT - Tasks List</h3>
            <a href="http://localhost:3000/addtask"><button className="addButton" >Add Task</button></a>
            <table className="table table-striped table-bordered">
                <thead>
                    <tr>
                        <th>Title</th>
                        <th>Description</th>
                        <th>Due Date</th>
                        <th>Completed</th>
                        <th>Edit Task</th>
                        <th>Delete Task</th>
                    </tr>
                </thead>
                <tbody>
                    {tasks && tasks.map(task =>
                        <tr key={task._id}>
                            <td>{task.name}</td>
                            <td width='30%'>{task.description}</td>
                            <td>{checkDate(task.dueTime)}
                            </td>
                            <td>
                                <button 
                                    className="buttonComplete"      // complete just deletes the task, sorry not sorry
                                    onClick={() => submitDelete(task)}> 
                                    Finish Task!
                                </button>
                            </td>
                            <td><a>
                                <button 
                                    className="buttonEdit" 
                                    onClick={() => editTask(task)}>
                                    Edit Task
                                    </button>
                                </a></td>
                            <td>
                                <button 
                                    className="buttons" 
                                    onClick={() => submitDelete(task)}> 
                                    Delete Task
                                </button>
                            </td>
                        </tr>
                    )}
                </tbody>
            </table>
            <button 
                className="buttons" 
                onClick={() => submitDeleteAll()}>
                Delete All tasks
            </button>
        </div>
    );
  }

  export default Tasks;