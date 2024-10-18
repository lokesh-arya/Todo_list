#Task Class - Here's the implementation of the Task class:
import json
import os


class Task:
    def __init__(self, title, description, category, completed):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed
    
    def mark_completed(self):
        self.completed = True
    
    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "completed": self.completed
        }
    
#Main Application Logic - implementing the main logic for managing tasks:
class TodoApp:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                tasks_data = json.load(file)
                return [Task(**task) for task in tasks_data]
        return []
    
    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file)
    
    def add_task(self, title, description, category, completed):
        task = Task(title, description, category, completed)
        self.tasks.append(task)
        self.save_tasks()
    
    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "✓" if task.completed else "✗"
            print(f"{i + 1}. {task.title} [{status}] - {task.category}: {task.description}")
    
    def edit_task(self, index, title=None, description=None, category=None):
        if 0 <= index < len(self.tasks):
            if title:
                self.tasks[index].title = title
            if description:
                self.tasks[index].description = description
            if category:
                self.tasks[index].category = category
            self.save_tasks()
    
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()
    
    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            self.save_tasks()

#User Interface - a simple command-line interface for user interaction.
def main():
    app = TodoApp()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            category = input("Enter task category: ")
            app.add_task(title, description, category, False)
        
        elif choice == '2':
            app.view_tasks()
        
        elif choice == '3':
            index = int(input("Enter task number to edit: ")) - 1
            title = input("New title (leave blank to keep current): ")
            description = input("New description (leave blank to keep current): ")
            category = input("New category (leave blank to keep current): ")
            app.edit_task(index, title if title else None, description if description else None, category if category else None)
        
        elif choice == '4':
            index = int(input("Enter task number to delete: ")) - 1
            app.delete_task(index)
        
        elif choice == '5':
            index = int(input("Enter task number to mark as completed: ")) - 1
            app.mark_completed(index)
        
        elif choice == '6':
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
