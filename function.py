# todo.py

import json
import os

class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed

    def mark_completed(self):
        self.completed = True

def load_tasks(filename='tasks.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            tasks_data = json.load(f)
            tasks = [Task(**task) for task in tasks_data]
    else:
        tasks = []
    return tasks

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as f:
        tasks_data = [task.__dict__ for task in tasks]
        json.dump(tasks_data, f, indent=4)

def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter task category (e.g., Work, Personal, Urgent): ")
    task = Task(title, description, category)
    tasks.append(task)
    print("Task added successfully.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
        return
    for idx, task in enumerate(tasks, 1):
        status = 'Completed' if task.completed else 'Not Completed'
        print(f"{idx}. [{status}] {task.title} - {task.category}")
        print(f"   Description: {task.description}")

def edit_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    task_number = int(input("Enter the task number to edit: "))
    if 1 <= task_number <= len(tasks):
        task = tasks[task_number - 1]
        print("Leave a field empty to keep it unchanged.")
        new_title = input(f"Enter new title (current: {task.title}): ") or task.title
        new_description = input(f"Enter new description (current: {task.description}): ") or task.description
        new_category = input(f"Enter new category (current: {task.category}): ") or task.category
        task.title = new_title
        task.description = new_description
        task.category = new_category
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    task_number = int(input("Enter the task number to delete: "))
    if 1 <= task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def mark_task_completed(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    task_number = int(input("Enter the task number to mark as completed: "))
    if 1 <= task_number <= len(tasks):
        task = tasks[task_number - 1]
        task.mark_completed()
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n=== Personal To-Do List Application ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            edit_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            mark_task_completed(tasks)
        elif choice == '6':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
        save_tasks(tasks)

if __name__ == "__main__":
    main()
