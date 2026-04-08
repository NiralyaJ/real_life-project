# Library Book Issue Tracker using Python (Tkinter)

## Description
The Library Book Issue Tracker is a simple and practical system developed using Python with a Graphical User Interface (GUI) using Tkinter. It allows users to record, manage, and track library book issue details such as book name, student name, and return status.

This project helps users efficiently manage library records and reduces manual errors. It demonstrates how Python programming and GUI development can be used to solve real-world problems like library management and record tracking.

---

## Objective
The main objectives of this project are:

- To help users manage library book records efficiently  
- To understand file handling using JSON in Python  
- To implement CRUD operations (Create, Read, Update, Delete)  
- To develop a real-time GUI-based application  
- To understand modular programming using functions  

The program is divided into functions such as:

- `add_record()`  
- `mark_returned()`  
- `refresh_list()`  
- `delete_record()`  

This improves code readability, maintenance, and reusability.

---

## Concepts Covered

This project helps in understanding:

- Data structures (lists and dictionaries)  
- File handling using JSON  
- GUI development using Tkinter  
- Error handling using try-except  
- Logical thinking and debugging  

---

## Features

### Library Management
- Add new book issue records  
- Track which student borrowed which book  
- Mark books as Returned  
- Delete records  

### Data Persistence
- Data stored in a file (`library.json`)  
- Data remains saved even after closing the application  

### Error Handling
- Handles invalid inputs  
- Prevents application crash  
- Displays user-friendly error messages  

### Record Tracking
- Displays issue/return status  
- Easy monitoring of library records  

---

## Technologies Used

- **Programming Language:** Python  
- **Libraries Used:**  
  - `tkinter` (for GUI)  
  - `json` (for data storage)  
  - `os` (for file handling)  
- **Interface:** Graphical User Interface (GUI)  

---

## System Architecture

The application follows a modular structure:

### Main Module
- Creates the main window  
- Handles user interface elements  

### Library Module
- Add book record  
- Mark book as returned  
- View records (Listbox display)  
- Delete record  

### File Handling Module
- Load data from JSON file  
- Save data to JSON file  

---

## File Structure


## Python Program

```
import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "library.json"

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

# Refresh list
def refresh_list():
    listbox.delete(0, tk.END)
    for item in data:
        status = "Returned" if item["returned"] else "Issued"
        listbox.insert(tk.END, f"{item['book']} - {item['student']} ({status})")

# Add record
def add_record():
    book = book_entry.get()
    student = student_entry.get()

    if book == "" or student == "":
        messagebox.showwarning("Warning", "Enter all fields")
        return

    data.append({
        "book": book,
        "student": student,
        "returned": False
    })

    save_data()
    refresh_list()

    book_entry.delete(0, tk.END)
    student_entry.delete(0, tk.END)

# Mark as returned
def mark_returned():
    try:
        index = listbox.curselection()[0]
        data[index]["returned"] = True
        save_data()
        refresh_list()
    except:
        messagebox.showerror("Error", "Select a record")

# Delete record
def delete_record():
    try:
        index = listbox.curselection()[0]
        removed = data.pop(index)
        save_data()
        refresh_list()
        messagebox.showinfo("Deleted", f"{removed['book']} removed")
    except:
        messagebox.showerror("Error", "Select a record")

# Main window
root = tk.Tk()
root.title("Library Tracker")
root.geometry("420x450")

data = load_data()

# UI
tk.Label(root, text="Book Name").pack()
book_entry = tk.Entry(root)
book_entry.pack()

tk.Label(root, text="Student Name").pack()
student_entry = tk.Entry(root)
student_entry.pack()

tk.Button(root, text="Add Record", command=add_record).pack(pady=5)

listbox = tk.Listbox(root, width=45)
listbox.pack(pady=10)

tk.Button(root, text="Mark as Returned", command=mark_returned).pack(pady=5)
tk.Button(root, text="Delete Record", command=delete_record).pack(pady=5)

# Load initial data
refresh_list()

root.mainloop()
```

## OUTPUT

<img width="516" height="588" alt="image" src="https://github.com/user-attachments/assets/897301d5-36bd-42f1-8159-5dde7f3e694f" />


<img width="517" height="585" alt="image" src="https://github.com/user-attachments/assets/191045a4-cce2-44fa-900c-dfd4802a7eda" />


## Result
The Library Book Issue Tracker is a simple yet effective application that demonstrates the use of Python, Tkinter, and JSON for building real-world systems. It improves understanding of GUI development, file handling, and modular programming.

## Author

Name: Niralya J
