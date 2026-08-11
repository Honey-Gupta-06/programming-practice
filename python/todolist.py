# ==============================
# TO-DO LIST APPLICATION
# Day 7 Python Project
# ==============================

tasks = []


# ------------------------------
# Add a task
# ------------------------------
def add_task():
    task = input("Enter task: ").strip()

    if task == "":
        print("Task cannot be empty.")
        return

    tasks.append({
        "task": task,
        "completed": False
    })

    print("Task added successfully!")


# ------------------------------
# View all tasks
# ------------------------------
def view_tasks():
    if len(tasks) == 0:
        print("\nNo tasks found.")
        return

    print("\n===== YOUR TASKS =====")

    for i, task in enumerate(tasks, start=1):

        if task["completed"]:
            status = "✓"
        else:
            status = " "

        print(f"{i}. [{status}] {task['task']}")


# ------------------------------
# Mark task as complete
# ------------------------------
def complete_task():
    if len(tasks) == 0:
        print("\nNo tasks available.")
        return

    view_tasks()

    try:
        number = int(input("\nEnter task number to complete: "))

        if 1 <= number <= len(tasks):

            if tasks[number - 1]["completed"]:
                print("Task is already completed.")
            else:
                tasks[number - 1]["completed"] = True
                print("Task completed successfully!")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# ------------------------------
# Delete a task
# ------------------------------
def delete_task():
    if len(tasks) == 0:
        print("\nNo tasks available.")
        return

    view_tasks()

    try:
        number = int(input("\nEnter task number to delete: "))

        if 1 <= number <= len(tasks):

            removed_task = tasks.pop(number - 1)

            print(
                f"Task '{removed_task['task']}' "
                "deleted successfully!"
            )

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# ------------------------------
# Main menu
# ------------------------------
while True:

    print("\n==============================")
    print("       TO-DO LIST APP")
    print("==============================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("\nThank you for using the To-Do List App!")
        break

    else:
        print("Invalid choice. Please select 1-5.")