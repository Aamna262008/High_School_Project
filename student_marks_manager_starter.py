"""Student Marks Manager - Starter Project

A beginner-friendly Python project for managing student marks.
Complete the functions marked TODO.

Recommended Python version: 3.10 or later
External packages: none
"""

import csv
from pathlib import Path


DATA_FILE = Path("students.csv")
SUBJECTS = ("English", "Mathematics", "Computer Science")
students = []


def calculate_grade(percentage):
    """Return a letter grade for a percentage."""
    if percentage >= 80:
        return "A"
    if percentage >= 70:
        return "B"
    if percentage >= 60:
        return "C"
    if percentage >= 50:
        return "D"
    return "F"


def get_valid_mark(subject):
    """Ask repeatedly until the user enters a number from 0 to 100."""
    while True:
        raw_value = input(f"Enter {subject} marks (0-100): ").strip()

        try:
            mark = float(raw_value)
        except ValueError:
            print("Please enter a number.")
            continue

        if 0 <= mark <= 100:
            return mark

        print("Marks must be between 0 and 100.")


def add_student():
    """Collect one student's marks and add the record to the list."""
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    marks = {}
    for subject in SUBJECTS:
        marks[subject] = get_valid_mark(subject)

    total = sum(marks.values())
    percentage = total / len(SUBJECTS)

    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": calculate_grade(percentage),
    }

    students.append(student)
    print(f"{name} was added successfully.")


def display_students():
    """Display all records currently stored in memory."""
    if not students:
        print("No student records are available.")
        return

    print("\nALL STUDENT RESULTS")
    print("-" * 70)

    for number, student in enumerate(students, start=1):
        marks = student["marks"]
        print(f"{number}. {student['name']}")
        print(
            f"   English: {marks['English']:.1f} | "
            f"Mathematics: {marks['Mathematics']:.1f} | "
            f"Computer Science: {marks['Computer Science']:.1f}"
        )
        print(
            f"   Total: {student['total']:.1f}/300 | "
            f"Percentage: {student['percentage']:.2f}% | "
            f"Grade: {student['grade']}"
        )
        print("-" * 70)


def search_student():
    """Find and display a student by name."""
    # TODO 1:
    # Ask for a name. Search students without worrying about capital letters.
    # Display the matching record, or print "Student not found".
    print("TODO: Build the student search feature.")


def show_class_average():
    """Calculate and display the average percentage of the whole class."""
    # TODO 2:
    # Handle an empty list first.
    # Hint: add all student percentages, then divide by len(students).
    print("TODO: Build the class average feature.")


def show_highest_scoring_student():
    """Display the student with the highest percentage."""
    # TODO 3:
    # Handle an empty list first.
    # Hint: max(students, key=...)
    print("TODO: Build the highest-scoring student feature.")


def save_results():
    """Save all student records to students.csv."""
    # TODO 4:
    # Use csv.DictWriter or csv.writer.
    # Suggested columns:
    # name, english, mathematics, computer_science, total, percentage, grade
    print("TODO: Save the results to students.csv.")


def load_results():
    """Load existing records from students.csv when the program starts."""
    # TODO 5:
    # 1. Check DATA_FILE.exists().
    # 2. Open the CSV file.
    # 3. Convert numeric text back to float.
    # 4. Append each reconstructed dictionary to students.
    # The program should still work when the file does not exist.
    pass


def print_menu():
    """Print the main menu."""
    print("\nSTUDENT MARKS MANAGER")
    print("1. Add student")
    print("2. Display all students")
    print("3. Search for a student")
    print("4. Show class average")
    print("5. Show highest-scoring student")
    print("6. Save results")
    print("7. Exit")


def main():
    """Run the menu until the user chooses Exit."""
    load_results()

    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            show_class_average()
        elif choice == "5":
            show_highest_scoring_student()
        elif choice == "6":
            save_results()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
