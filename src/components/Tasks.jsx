import React, {useState} from "react";
import "../index.css"
import "./css/Tasks.css"


function Tasks() {
    // tasks API not implemented yet but will return JSON in this form for future reference
    // {{id_1, title_1, due_data_1, ...}, {id_2, title_2, due_date_2, ...}, {id_3, title_3, due_data_3, ...}}
    const [tasks, setTasks] = useState([
        { id: 1, title: 'task_1', due_date: '01/12/2021', completed: true },
        { id: 2, title: 'task_2', due_date: '01/12/2021', completed: false },
        { id: 3, title: 'task_3', due_date: '01/12/2021', completed: true },
        { id: 4, title: 'task_4', due_date: '01/12/2021', completed: false },
        { id: 5, title: 'task_5', due_date: '01/12/2021', completed: false },
        { id: 5, title: 'task_7', due_date: '01/12/2021', completed: false },
        { id: 5, title: 'task_8', due_date: '01/12/2021', completed: false },
        { id: 5, title: 'task_9', due_date: '01/12/2021', completed: false }
    ]);

    // Returns a conditional render of the completed status of a task
    function renderCompleted(completed) {
        if (completed) {
          return <td>Yes</td>;
        } else {
          return <td>No</td>;
        }
    }


    return (
        <div className="container">
            <h3 className="p-3 text-center">DO-IT - Tasks List</h3>
            <a href="http://localhost:3000/addtask"><button className="addButton" >Add Task</button></a>
            <a href="http://localhost:3000/tasks"><button className="weeklyButton" >Weekly View</button></a>
            <a href="http://localhost:3000/tasks"><button className="monthlyButton" >Monthly View</button></a>
            <a href="http://localhost:3000/tasks"><button className="dailyButton" >Daily View</button></a>
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
                            <td>{task.title}</td>
                            <td>{task.due_date}</td>
                            {renderCompleted(task.completed)}
                            <td><a href="http://localhost:3000/edittask"><button className="buttons" >Edit Task</button></a></td>
                            <td><a href="http://localhost:3000/tasks"><button className="buttons" >Delete Task</button></a></td>
                        </tr>
                    )}
                </tbody>
            </table>
        </div>
    );
  }

  export default Tasks;