#!/usr/bin/env python3
"""
ToDo List application
import module serializes and deserializes Python objects
to save/load to/from file
"""
import pickle

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} - {status}"

class ToDoList:
    """
    reps the entire to-do list
    """
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        # Create a new Task object and add it to the tasks list
        task = Task(title, description)
        self.tasks.append(task)

    def list_tasks(self):
        # Print each task in the tasks list
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def update_task(self, index, title, description, completed):
        # Update an existing task at the specified index
        task = self.tasks[index]
        task.title = title
        task.description = description
        task.completed = completed

    def delete_task(self, index):
        # Delete the task at the specified index
        del self.tasks[index]

    def save_to_file(self, filename):
        # Serialize and save tasks list to a file using pickle
        with open(filename, "wb") as f:
            pickle.dump(self.tasks, f)

    def load_from_file(self, filename):
        # Load tasks list from a file and deserialize using pickle
        with open(filename, "rb") as f:
            self.tasks = pickle.load(f)

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task\n2. List Tasks\n3. Update Task\n4. Delete Task\n5. Save to File\n6. Load from File\n7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
        elif choice == "2":
            todo_list.list_tasks()
        elif choice == "3":
            index = int(input("Enter the index of the task to update: "))
            title = input("Enter new title: ")
            description = input("Enter new description: ")
            completed = input("Is task completed? (True/False): ").lower() == "true"
            todo_list.update_task(index - 1, title, description, completed)
        elif choice == "4":
            index = int(input("Enter the index of the task to delete: "))
            todo_list.delete_task(index - 1)
        elif choice == "5":
            filename = input("Enter filename to save: ")
            todo_list.save_to_file(filename)
            print("Tasks saved to file successfully.")
        elif choice == "6":
            filename = input("Enter filename to load: ")
            todo_list.load_from_file(filename)
            print("Tasks loaded from file successfully.")
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
