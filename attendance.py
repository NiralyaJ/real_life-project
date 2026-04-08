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