import logo from './logo.svg';
import './App.css';
import {useState} from "react";
/*
Task 2 - FrontEnd
Implement a simple to-do list application in React. The application should allow users to #add and delete items #
from the list. The list items should be stored in the #component's state#. Demonstrate the use of React hooks to
manage state and handle user actions.
 */
function App() {

    const [tasks, setTasks] = useState([]);
    const [newTask, setNewTask] = useState('');
    const handleInputTaskChange = (event) => {
        setNewTask(event.target.value);
        };

    // Adding item to the list
    const AddTask = () => {
        if (newTask.trim()) {  // Validate the input if it is not empty
            // call the setItems
            setTasks((prevItems) => [...prevItems, newTask]);
            setNewTask(''); // clear the input field
        }

    }
    //Allow user to delete task
    const deleteTask = (index) => {
        setTasks(tasks.filter((task) => task !== tasks[index]));

    }
  return (

         <div className="App">
        <h3>simple to-do task list application in React - task2 </h3>
     <div>
        <input
          type="text"
          value={newTask}
          onChange={handleInputTaskChange}
          placeholder="Enter a new Task"
        />
        <button class='submittask' onClick={AddTask}> Add task</button>
      </div>
    <div class = 'list'>
     <ul>
        {tasks.map((task, index) => (
          <li key={index}>
            {task}
            <button class='delete-button' onClick={() => deleteTask(index)}>Delete</button>
          </li>
        ))}
      </ul>
  </div>


    </div>
  );
}

export default App;
