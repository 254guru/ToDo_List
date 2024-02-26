# To-Do List Application

## Overview
This is a simple command-line To-Do List application implemented in Python. It allows users to manage their tasks efficiently by providing functionalities to add tasks, list tasks, update tasks, delete tasks, save tasks to a file, and load tasks from a file.

## Prerequisites
- Python 3.x
- pickle (for serialization, already included in Python standard library)

## Usage
1. **Run the program**: 
    - Open a terminal or command prompt.
    - Navigate to the directory where the `todo_list_app.py` file is located.
    - Run the program by typing `python todo_list_app.py` and pressing Enter.

2. **Interact with the program**:
    - Once the program is running, you'll see a menu with options to perform various tasks.
    - Follow the prompts to add tasks, list tasks, update tasks, delete tasks, save tasks to a file, or load tasks from a file.
    - To exit the program, select the option to exit from the menu.

## Functionalities
- **Add Task**: Add a new task to the to-do list with a title and description.
- **List Tasks**: View all tasks in the to-do list along with their statuses (completed or pending).
- **Update Task**: Modify an existing task's title, description, or completion status.
- **Delete Task**: Remove a task from the to-do list.
- **Save to File**: Save the current state of the to-do list to a file for future use.
- **Load from File**: Load tasks from a file and restore the to-do list to a previous state.

## Implementation Details
- The application consists of two classes: `Task` and `ToDoList`.
- `Task` class represents an individual task with attributes such as title, description, and completion status.
- `ToDoList` class manages the list of tasks and provides methods to perform various operations on tasks.
- Tasks are stored in a list within the `ToDoList` class.
- Task data is serialized and deserialized using the `pickle` module for saving and loading from files.

## Sample Usage
		1.Add Task
		2.List Tasks
		3.Update Task
		4.Delete Task
		5.Save to File
		6.Load from File
		7.Exit
		Enter your choice: 1
		Enter task title: Complete project
		Enter task description: Finish the To-Do List application


## Author
- [Kevin Oluda](https://github.com/254guru)

Feel free to contribute or provide feedback!

