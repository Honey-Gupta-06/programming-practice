import json
import os

FILE_NAME = "students.json"


# Load students from JSON file
def load_students():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


# Save students to JSON file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Add a student
def add_student():
    name = input("Enter student name: ")
    
    try:
        age = int(input("Enter student age: "))
    except ValueError:
        print("Please enter a valid age.")
        return

    course = input("Enter student course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students = load_students()
    students.append(student)
    save_students(students)

    print("Student added successfully!")


# View all students
def view_students():
    students = load_students()

    if len(students) == 0:
        print("No students found.")
        return

    print("\n===== Student List =====")

    for i, student in enumerate(students, start=1):
        print(f"\nStudent {i}")
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])


# Main program
while True:

    print("\n==============================")
    print("   STUDENT JSON DATABASE")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please select 1-3.")