# Study Deadline Checker
# A beginner Python project that reads homework deadlines from tasks.csv
# and shows what is overdue or coming soon.

import csv
import datetime 
from datetime import date
import os

# Always use the tasks.csv sitting next to this script,
# no matter which folder the program is run from.
FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.csv")


def create_file_if_missing(filename):
    # If the file already exists, do nothing and use it as it is.
    if os.path.exists(filename):
        return
    # If it is missing, create it with just the header row
    # so the rest of the program never crashes.
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["subject", "task", "due_date", "completed"])


def load_tasks(filename):
    # If the file does not exist, there are no tasks yet.
    if not os.path.exists(filename):
        return []
    tasks = []
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            tasks.append(row)
    return tasks


def sort_tasks(tasks, today):
    # Decide which bucket each task belongs in, without printing anything.
    # Returning the buckets makes this easy to test.
    completed_count = 0
    overdue = []
    upcoming = []

    for task in tasks:
        if task["completed"] == "yes":
            completed_count = completed_count + 1
            continue  # completed tasks are never overdue or upcoming
        due = datetime.date.fromisoformat(task["due_date"])
        if due < today:
            overdue.append(task)
        elif due <= today + datetime.timedelta(days=7):
            upcoming.append(task)

    return overdue, upcoming, completed_count


def show_report(tasks, today):
    overdue, upcoming, completed_count = sort_tasks(tasks, today)

    print()
    print("OVERDUE")
    for task in overdue:
        print("- " + task["subject"] + ": " + task["task"]
              + " (due " + task["due_date"] + ")")

    print()
    print("UPCOMING - NEXT 7 DAYS")
    for task in upcoming:
        print("- " + task["subject"] + ": " + task["task"]
              + " (due " + task["due_date"] + ")")

    print()
    print("Completed tasks:", completed_count)


def add_task(filename):
    subject = input("Subject: ")
    task = input("Task: ")

    # Keep asking until the date is in the correct YYYY-MM-DD format.
    while True:
        due_date = input("Due date (YYYY-MM-DD): ")
        try:
            datetime.date.fromisoformat(due_date)
            break  # the date is valid, leave the loop
        except ValueError:
            print("That is not a valid date. Please use YYYY-MM-DD.")

    # Keep asking until the answer is exactly yes or no.
    while True:
        completed = input("Completed? (yes/no): ").lower()
        if completed == "yes" or completed == "no":
            break
        print("Please answer yes or no.")

    # Append means: add one row at the end, keep everything already there.
    with open(filename, "a", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["subject", "task", "due_date", "completed"])
        writer.writerow({"subject": subject, "task": task,
                         "due_date": due_date, "completed": completed})
    print("Task added!")


def main():
    while True:
        print()
        print("STUDY DEADLINE CHECKER")
        print("----------------------")
        print("1. View deadline report")
        print("2. Add a task")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            tasks = load_tasks(FILENAME)
            today = date.today()
            show_report(tasks, today)
        elif choice == "2":
            add_task(FILENAME)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2, or 3.")


if __name__ == "__main__":
    create_file_if_missing(FILENAME)
    main()