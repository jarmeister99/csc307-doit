import React, {useState, useEffect} from "react";
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

    // Returns a conditional render of the completed status of a task
    function renderCompleted(completed) {
        if (completed) {
          return <td>Yes</td>;
        } else {
          return <td>No</td>;
        }
    }

    async function fetchAll(){
        try {
           const response = await axios.get('http://localhost:5000/tasks', {withCredentials: true});
           return response.data;
        }
        catch (error){
           //We're not handling errors. Just logging into the console.
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
                        <th>Due Date</th>
                        <th>Completed</th>
                        <th>Edit Task</th>
                        <th>Delete Task</th>
                    </tr>
                </thead>
                <tbody>
                    {tasks && tasks.map(task =>
                        <tr key={task.id}>
                            <td>{task.name}</td>
                            <td>{task.dueTime}</td>
                            {renderCompleted(task.completed)}
                            <td><a href="http://localhost:3000/edittask"><button className="buttons" >Edit Task</button></a></td>
                            <td><a href="http://localhost:3000/deletetask"><button className="buttons" >Delete Task</button></a></td>
                        </tr>
                    )}
                </tbody>
            </table>
        </div>
    );
  }

  export default Tasks;