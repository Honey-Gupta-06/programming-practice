import pandas as pd


# -----------------------------------
# Empty student DataFrame
# -----------------------------------

df = pd.DataFrame(columns=["Name", "Age", "Marks", "Course"])


# -----------------------------------
# Add Student
# -----------------------------------

def add_student():
    global df

    name = input("Enter student name: ")

    try:
        age = int(input("Enter student age: "))
        marks = float(input("Enter student marks: "))
    except ValueError:
        print("Age and marks must be numbers.")
        return

    course = input("Enter student course: ")

    new_student = pd.DataFrame({
        "Name": [name],
        "Age": [age],
        "Marks": [marks],
        "Course": [course]
    })

    df = pd.concat([df, new_student], ignore_index=True)

    print("\nStudent added successfully!")


# -----------------------------------
# View all students
# -----------------------------------

def view_students():
    if df.empty:
        print("\nNo student data available.")
        return

    print("\n===== STUDENT DATA =====")
    print(df.to_string(index=False))


# -----------------------------------
# Show average marks
# -----------------------------------

def average_marks():
    if df.empty:
        print("\nNo student data available.")
        return

    average = df["Marks"].mean()

    print("\nAverage Marks:", round(average, 2))


# -----------------------------------
# Show highest marks
# -----------------------------------

def highest_marks():
    if df.empty:
        print("\nNo student data available.")
        return

    student = df.loc[df["Marks"].idxmax()]

    print("\n===== TOP STUDENT =====")
    print("Name:", student["Name"])
    print("Marks:", student["Marks"])
    print("Course:", student["Course"])


# -----------------------------------
# Show lowest marks
# -----------------------------------

def lowest_marks():
    if df.empty:
        print("\nNo student data available.")
        return

    student = df.loc[df["Marks"].idxmin()]

    print("\n===== LOWEST SCORER =====")
    print("Name:", student["Name"])
    print("Marks:", student["Marks"])
    print("Course:", student["Course"])


# -----------------------------------
# Students above 80
# -----------------------------------

def high_scorers():
    if df.empty:
        print("\nNo student data available.")
        return

    students = df[df["Marks"] > 80]

    if students.empty:
        print("\nNo students scored above 80.")
    else:
        print("\n===== STUDENTS ABOVE 80 =====")
        print(students.to_string(index=False))


# -----------------------------------
# Students by course
# -----------------------------------

def course_count():
    if df.empty:
        print("\nNo student data available.")
        return

    print("\n===== STUDENTS BY COURSE =====")
    print(df["Course"].value_counts())


# -----------------------------------
# Main Menu
# -----------------------------------

while True:

    print("\n==============================")
    print("     STUDENT DATA ANALYSIS")
    print("==============================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Average Marks")
    print("4. Highest Marks")
    print("5. Lowest Marks")
    print("6. Students Above 80")
    print("7. Students By Course")
    print("8. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        average_marks()

    elif choice == "4":
        highest_marks()

    elif choice == "5":
        lowest_marks()

    elif choice == "6":
        high_scorers()

    elif choice == "7":
        course_count()

    elif choice == "8":
        print("\nThank you for using Student Data Analysis!")
        break

    else:
        print("\nInvalid choice. Please select 1-8.")