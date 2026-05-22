# Student Record Management System

import json

FILE_NAME = "students.json"

students = []


def load_data():
    global students
    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)
    except:
        students = []


def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")

    student = {
        "roll": roll,
        "name": name,
        "course": course
    }

    students.append(student)
    save_data()
    print("Student added successfully.")


def search_student():
    roll = input("Enter Roll Number to search: ")

    for student in students:
        if student["roll"] == roll:
            print(student)
            return

    print("Student not found.")


def delete_student():
    roll = input("Enter Roll Number to delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            save_data()
            print("Student deleted successfully.")
            return

    print("Student not found.")


load_data()

while True:
    print("\n===== Student Record Management =====")
    print("1. Add Student")
    print("2. Save Student Data")
    print("3. Load Data From File")
    print("4. Search Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        save_data()
        print("Data saved successfully.")

    elif choice == "3":
        load_data()
        print("Data loaded successfully.")
        print(students)

    elif choice == "4":
        search_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
