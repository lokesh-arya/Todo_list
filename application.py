import tkinter as tk
from ToDo_List import *

app = TodoApp()
root = tk.Tk()

root.title('Personal TO-DO List')
root.geometry('500x600')

def cancel_function():
    for child in edit_window.winfo_children():
        child.destroy()
    for child in add_task_window.winfo_children():
        child.destroy()
    edit_window.pack_forget()
    add_task_window.pack_forget()
    window.pack()

def save_function(index, title, description, category):
    if index:
        task_list[index].title = str(title.get())
        task_list[index].description = str(description.get())
        task_list[index].category = str(category.get())
        app.save_tasks()
    else:
        app.add_task(str(title.get()), str(description.get()), str(category.get()), False)

    for child in edit_window.winfo_children():
        child.destroy()
    for child in add_task_window.winfo_children():
        child.destroy()
    edit_window.pack_forget()
    add_task_window.pack_forget()
    window.pack()
    destory_all_task()
    display_task(task_list)
    print("done")

def add_task_function():
    window.pack_forget()
    add_task_window.pack()

    title_var = tk.StringVar()
    description_var = tk.StringVar()
    category_var = tk.StringVar()

    tk.Label(add_task_window, text='Description').grid(row=1,column=0)
    tk.Label(add_task_window, text='Title').grid(row=0,column=0)
    tk.Label(add_task_window, text='Category').grid(row=2,column=0)
    tk.Entry(add_task_window, textvariable=title_var).grid(row=0,column=1)
    tk.Entry(add_task_window, textvariable=description_var).grid(row=1,column=1)
    tk.Entry(add_task_window, textvariable=category_var).grid(row=2,column=1)

    cancel_button = tk.Button(add_task_window,text='Cancel', command=lambda: cancel_function())
    save_button = tk.Button(add_task_window,text='Save', command=lambda: save_function(False, title_var, description_var, category_var))
    cancel_button.grid(row=3, column=0)
    save_button.grid(row=3, column=1)

def edit_task(index):
    window.pack_forget()
    edit_window.pack()
    
    title_var = tk.StringVar()
    title_var.set(task_list[index].title)
    description_var = tk.StringVar()
    description_var.set(task_list[index].description)
    category_var = tk.StringVar()
    category_var.set(task_list[index].category)

    tk.Label(edit_window, text='Description').grid(row=1,column=0)
    tk.Label(edit_window, text='Title').grid(row=0,column=0)
    tk.Label(edit_window, text='Category').grid(row=2,column=0)
    tk.Entry(edit_window, textvariable=title_var).grid(row=0,column=1)
    tk.Entry(edit_window, textvariable=description_var).grid(row=1,column=1)
    tk.Entry(edit_window, textvariable=category_var).grid(row=2,column=1)

    cancel_button = tk.Button(edit_window,text='Cancel', command=lambda: cancel_function())
    save_button = tk.Button(edit_window,text='Save', command=lambda: save_function(index, title_var, description_var, category_var))
    cancel_button.grid(row=3, column=0)
    save_button.grid(row=3, column=1)

def mark_complete_task(index):
    app.mark_completed(index)
    destory_all_task()
    display_task(task_list)
    print("done")

def delete_task(index):
    app.delete_task(index)
    destory_all_task()
    display_task(task_list)
    print("done")

def task_frame(frame, task, index):
    task_box = tk.Frame(frame, bg='lightblue')
    task_box.pack(padx=10, pady=10, fill='x')

    title_label = tk.Label(task_box, text=task.title, bg='lightgreen',justify=tk.LEFT)
    title_label.pack(padx=10, pady=10, fill='x')

    content = tk.Label(task_box, text=task.description, bg='red', wraplength=400, justify=tk.LEFT)
    content.pack(padx=10, pady=10, fill='x')

    footer = tk.Frame(task_box, bg='grey')
    footer.pack(padx=10, pady=10, fill='x')

    status = "Completed ✓" if task.completed else "Incomplete"
    completed_lable = tk.Label(footer, text=status, bg='green',)
    completed_lable.pack(padx=10, pady=10, side=tk.LEFT)

    if status == "Incomplete":
        completed_button = tk.Button(footer, text="Mark Complete", command=lambda: mark_complete_task(index), bg='lightblue')
        completed_button.pack(padx=10, pady=10, side=tk.LEFT)
    
    edit_button = tk.Button(footer, text='Edit',command=lambda: edit_task(index), bg='lightblue')
    edit_button.pack(padx=10, pady=10, side=tk.LEFT)

    delete_button = tk.Button(footer, text='Delete', command=lambda: delete_task(index), bg='lightblue')
    delete_button.pack(padx=10, pady=10, side=tk.LEFT)

def display_task(task_list):
    for i in range(len(task_list)):
        if task_list[i].category == 'work':
            task_frame(work_frame, task_list[i], index=i)

        if task_list[i].category == 'personal':
            task_frame(personal_frame, task_list[i], index=i)

        if task_list[i].category == 'urgent':
            task_frame(work_frame, task_list[i], index=i)

def destory_all_task():
    for child in work_frame.winfo_children():
        child.destroy()
    for child in personal_frame.winfo_children():
        child.destroy()
    for child in urgent_frame.winfo_children():
        child.destroy()

def show_frame(frame):
    # Hide all frames
    for f in frames:
        f.pack_forget()
    # Show the selected frame
    frame.pack(fill='both', expand=True)

# Create the main window
window = tk.Frame(root)
window.pack(fill='both',expand=True)
edit_window = tk.Frame(root)
add_task_window = tk.Frame(root)
menu = tk.Frame(window, bg='lightblue')
menu.pack(fill='x')

# category button
btn_work = tk.Button(menu, text="Work", command=lambda: show_frame(work_frame))
btn_personal = tk.Button(menu, text="Personal", command=lambda: show_frame(personal_frame))
btn_urgent = tk.Button(menu, text="Urgent", command=lambda: show_frame(urgent_frame))
btn_add_task = tk.Button(menu, text='[+] Add Task', command=lambda: add_task_function())

btn_work.pack(side=tk.LEFT, padx=5, pady=5)
btn_personal.pack(side=tk.LEFT, padx=5, pady=5)
btn_urgent.pack(side=tk.LEFT, padx=5, pady=5)
btn_add_task.pack(side=tk.RIGHT, padx=5, pady=5)

# Create frames
work_frame = tk.Frame(window, bg='red')
personal_frame = tk.Frame(window, bg='green')
urgent_frame = tk.Frame(window, bg='blue')

# Store frames in a list
frames = [work_frame, personal_frame, urgent_frame]

row = {'title':'hello', 'content':'testing lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem', 'category':'work'}
task_list = app.tasks
display_task(task_list)

# Start with the first frame
show_frame(work_frame)

root.mainloop()
