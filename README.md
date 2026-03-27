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
python
import json
import os

FILE_NAME = "attendance.json"

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file)

def add_student(data):
    name = input("Enter student name: ")
    data.append({"name": name, "present": False})
    save_data(data)
    print("Student added successfully!")

def view_students(data):
    if not data:
        print("No students found.")
        return

    print("\nStudent List:")
    for i, s in enumerate(data):
        status = "Present" if s["present"] else "Absent"
        print(f"{i+1}. {s['name']} - {status}")

def mark_attendance(data):
    view_students(data)
    try:
        num = int(input("Enter student number to mark present: "))
        data[num-1]["present"] = True
        save_data(data)
        print("Attendance marked!")
    except:
        print("Invalid input!")

def delete_student(data):
    view_students(data)
    try:
        num = int(input("Enter student number to delete: "))
        removed = data.pop(num-1)
        save_data(data)
        print(f"Deleted student: {removed['name']}")
    except:
        print("Invalid input!")

def main():
    data = load_data()

    while True:
        print("\n==== ATTENDANCE TRACKER ====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Mark Attendance")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            mark_attendance(data)
        elif choice == "4":
            delete_student(data)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
```

## OUTPUT

<img width="497" height="496" alt="image" src="https://github.com/user-attachments/assets/1348e57e-9eba-4c3c-9ce3-03f1ab0e2fe3" />

<img width="606" height="437" alt="image" src="https://github.com/user-attachments/assets/15291f7b-fc88-42fa-b424-816ae57c0bb2" />

## Result
The Student Attendance Tracker using Python is a useful application for managing student attendance efficiently. It demonstrates important programming concepts such as file handling, modular programming, and data management. This project serves as a foundation for building more advanced academic management systems.

## Author

Name: Niralya J
