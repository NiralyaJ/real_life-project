# Student Attendance Tracker using Python

## Description
The Student Attendance Tracker is a simple and practical system developed using Python. It allows users to record, manage, and track student attendance through a Command-Line Interface (CLI).

This project helps teachers or users maintain attendance records efficiently and reduces manual errors. It demonstrates how programming concepts can be used to solve real-world problems like attendance management and record keeping.

---

## Objective

The main objectives of this project are:

- To help users manage student attendance efficiently  
- To understand file handling in Python  
- To implement CRUD operations (Create, Read, Update, Delete)  
- To develop a real-time usable application  
- To understand modular programming  

The program is divided into functions such as:
- add_student()  
- mark_attendance()  
- view_attendance()  
- delete_student()  

This improves code readability, maintenance, and reusability.

The project also helps in understanding:
- Data structures  
- File handling  
- Error handling  
- Logical thinking and debugging  

---

## Features

Attendance Management  
- Add new students  
- Mark attendance (Present/Absent)  
- View attendance records  
- Delete student records  

Data Persistence  
- Data stored in a file (attendance.json)  
- Data remains after closing the program  

Error Handling  
- Handles invalid inputs  
- Prevents program crash  

Attendance Tracking  
- Displays attendance status  
- Easy monitoring of student records  

---

## Technologies Used

Programming Language: Python  

Libraries Used:  
- json (for storing data)  
- os (for file handling)  

Interface: Command Line Interface (CLI)  

---

## System Architecture

The application follows a modular structure:

Main Module  
- Displays menu  
- Takes user input  

Attendance Module  
- Add student  
- Mark attendance  
- View attendance  
- Delete student  

File Handling Module  
- Load data from file  
- Save data to file  

---

## Python Program

```
import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "attendance.json"

# Load data
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save data
def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(data, file)

# Refresh listbox
def refresh_list():
    listbox.delete(0, tk.END)
    for s in data:
        status = "Present" if s["present"] else "Absent"
        listbox.insert(tk.END, f"{s['name']} - {status}")

# Add student
def add_student():
    name = entry.get()
    if name == "":
        messagebox.showwarning("Warning", "Enter a name")
        return
    data.append({"name": name, "present": False})
    save_data()
    refresh_list()
    entry.delete(0, tk.END)

# Mark attendance
def mark_present():
    try:
        index = listbox.curselection()[0]
        data[index]["present"] = True
        save_data()
        refresh_list()
    except:
        messagebox.showerror("Error", "Select a student")

# Delete student
def delete_student():
    try:
        index = listbox.curselection()[0]
        removed = data.pop(index)
        save_data()
        refresh_list()
        messagebox.showinfo("Deleted", f"{removed['name']} removed")
    except:
        messagebox.showerror("Error", "Select a student")

# Main window
root = tk.Tk()
root.title("Attendance Tracker")
root.geometry("400x400")

data = load_data()

# UI Elements
tk.Label(root, text="Enter Student Name").pack()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Add Student", command=add_student).pack(pady=5)

listbox = tk.Listbox(root, width=40)
listbox.pack(pady=10)

tk.Button(root, text="Mark Present", command=mark_present).pack(pady=5)
tk.Button(root, text="Delete Student", command=delete_student).pack(pady=5)

# Initial load
refresh_list()

root.mainloop()
```

## OUTPUT

<img width="497" height="496" alt="image" src="https://github.com/user-attachments/assets/1348e57e-9eba-4c3c-9ce3-03f1ab0e2fe3" />

<img width="606" height="437" alt="image" src="https://github.com/user-attachments/assets/15291f7b-fc88-42fa-b424-816ae57c0bb2" />

## Result
The Student Attendance Tracker using Python is a useful application for managing student attendance efficiently. It demonstrates important programming concepts such as file handling, modular programming, and data management. This project serves as a foundation for building more advanced academic management systems.

## Author

Name: Niralya J
