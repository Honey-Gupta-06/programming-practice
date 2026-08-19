import json
import os
from datetime import datetime

FILE = "study_data.json"


def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            return json.load(file)
    return []


def save_data(data):
    with open(FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_session(data):
    subject = input("Enter subject: ")
    
    try:
        minutes = int(input("Enter study time (minutes): "))
    except ValueError:
        print("Please enter a valid number.")
        return

    session = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "subject": subject,
        "minutes": minutes
    }

    data.append(session)
    save_data(data)

    print("✅ Study session saved!")


def show_summary(data):
    if not data:
        print("No study sessions recorded yet.")
        return

    total_minutes = sum(session["minutes"] for session in data)

    subjects = {}

    for session in data:
        subject = session["subject"]
        subjects[subject] = subjects.get(subject, 0) + session["minutes"]

    print("\n========== STUDY SUMMARY ==========")
    print(f"Total study time: {total_minutes} minutes")
    print(f"Total study time: {total_minutes / 60:.2f} hours")

    print("\nSubject-wise time:")

    for subject, minutes in subjects.items():
        print(f"{subject}: {minutes} minutes")

    best_subject = max(subjects, key=subjects.get)

    print(f"\n🏆 Most studied subject: {best_subject}")


def show_history(data):
    if not data:
        print("No study history available.")
        return

    print("\n========== STUDY HISTORY ==========")

    for session in data:
        print(
            f"{session['date']} | "
            f"{session['subject']} | "
            f"{session['minutes']} minutes"
        )


def main():
    data = load_data()

    while True:
        print("\n==============================")
        print("       STUDY TRACKER")
        print("==============================")
        print("1. Add Study Session")
        print("2. Show Summary")
        print("3. Show History")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_session(data)

        elif choice == "2":
            show_summary(data)

        elif choice == "3":
            show_history(data)

        elif choice == "4":
            print("Goodbye! Keep studying 📚")
            break

        else:
            print("Invalid choice. Try again.")


main()