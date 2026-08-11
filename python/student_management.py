class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("\n--------------------")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("--------------------")


students = []


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter student course: ")

    student = Student(name, age, course)
    students.append(student)

    print("Student added successfully!")


def view_students():
    if len(students) == 0:
        print("No students found.")
        return

    print("\n===== Student List =====")

    for student in students:
        student.display()


while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")