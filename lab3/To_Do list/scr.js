const taskInput = document.querySelector("#new-todo");
const addTaskBtn = document.querySelector("#add-todo");
const taskList = document.querySelector("#list-todo");

let tasks = [
  { name: "Go to University", done: false },
  { name: "Training", done: false },
  { name: "Study", done: false },
];

const addTask = () => {
  const newTaskName = taskInput.value.trim();
  if (newTaskName === "") {
    alert("Error: Empty input");
    return;
  }
  tasks.push({ name: newTaskName, done: false });
  renderTasks();
  taskInput.value = "";
};

const markTaskDone = (index) => {
  tasks[index].done = !tasks[index].done;
  renderTasks();
};

const deleteTask = (index) => {
  tasks.splice(index, 1);
  renderTasks();
};

const renderTasks = () => {
  taskList.innerHTML = "";
  tasks.forEach((task, index) => {
    const taskItem = document.createElement("li");
    taskItem.classList.add("task-item");

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = task.done;
    checkbox.addEventListener("change", () => {
      markTaskDone(index);
    });

    const taskName = document.createElement("div");
    taskName.classList.add("item");
    if (task.done) {
      taskName.classList.add("done");
    }
    taskName.textContent = task.name;

    const deleteBtn = document.createElement("div");
    deleteBtn.classList.add("delete-btn");
    deleteBtn.innerHTML = '<i class="fas fa-trash"></i>';
    deleteBtn.addEventListener("click", () => {
      deleteTask(index);
    });

    taskItem.appendChild(checkbox);
    taskItem.appendChild(taskName);
    taskItem.appendChild(deleteBtn);
    taskList.appendChild(taskItem);
  });
};

addTaskBtn.addEventListener("click", addTask);

renderTasks();
