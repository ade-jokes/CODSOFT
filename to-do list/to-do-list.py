import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

def add_task():
    task = task_entry.get()
    task_entry.delete(0, 'end')

    if task:
        with open('tasklist.txt', 'a') as taskfile:
            taskfile.write(f"{task}\n")
        task_list.append(task)
        listbox.insert('end', task)

def delete_task():
    task = str(listbox.get(listbox.curselection()))
    if task in task_list:
        task_list.remove(task)
        with open('tasklist.txt', 'w') as taskfile:
            for task in task_list:
                taskfile.write(f"{task}\n")
        listbox.delete(listbox.curselection())

def open_task_file():
    try:
        global task_list
        with open('tasklist.txt', 'r') as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task!= '\n':
                task_list.append(task.strip())
                listbox.insert("end", task_list[-1])

    except:
        with open('tasklist.txt', 'w') as taskfile:
            pass

def delete_icon_command():
    for file in os.listdir():
        if file.endswith('.txt'):
            os.remove(file)
    task_list.clear()
    listbox.delete(0, 'end')

def save_task_list():
    with open('tasklist.txt', 'w') as taskfile:
        for task in task_list:
            taskfile.write(f"{task}\n")

# Icons
img_icon = ImageTk.PhotoImage(file="to-do list/task.png")
root.iconphoto(False, img_icon)

note = ImageTk.PhotoImage(file="to-do list/task.png")
background = ImageTk.PhotoImage(file="to-do list/img.jpg")
bar_icon = ImageTk.PhotoImage(file="to-do list/top-bar.jpeg")
dock_icon = ImageTk.PhotoImage(file="to-do list/dock.jpg")
delete_icon = ImageTk.PhotoImage(file="to-do list/delete.jpeg")

# Labels
back_Label = tk.Label(root, image=background)
back_Label.place(x=0, y=0)

note_label = tk.Label(root, image=note)
note_label.place(x=30, y=25)

tskLabel = tk.Label(root, image=img_icon)

barLabel = tk.Label(root, image=bar_icon)
barLabel.place(x=0, y=0)

dock_img = tk.Label(root, image=dock_icon, bg='#32405b')
dock_img.place(x=30, y=25)

# Main
heading = tk.Label(root, text='ALL TASK', font='arial 20 bold', fg='white', bg='#32405b')
heading.place(x=130, y=20)

frame = tk.Frame(root, width=400, height=50, bg='white')
frame.place(x=0, y=180)

task = tk.StringVar()
task_entry = tk.Entry(frame, width=18, font='arial 20', bd=0, textvariable=task)
task_entry.place(x=10, y=7)
task_entry.focus()

button = tk.Button(frame, text='ADD', font='arial 20 bold', width=6, bg='#5a95ff', fg='#fff', bd=0, command=add_task)
button.place(x=300, y=0)

# Listbox
frame1 = tk.Frame(root, bd=3, width=700, height=280, bg='#32405b')
frame1.pack(pady=(240, 0))

listbox = tk.Listbox(frame1, font=('arial', 12), width=40, height=16, bg='#32405b', fg='white', cursor='hand2', selectbackground='#5a95ff')
listbox.pack(side='left', fill='both', padx=2)

scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side='right', fill='both')

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Delete button
delete_button = tk.Button(root, image=delete_icon, command=delete_icon_command, bd=0)
delete_button.pack(side='bottom', pady=13)

# Initialization
open_task_file()
root.mainloop()