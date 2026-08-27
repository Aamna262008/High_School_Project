# Simple Expense Tracker
# A beginner Python project that reads expenses from expenses.csv,
# shows spending totals, and can create a text report

import csv
import datetime
import os
import sys

# Always use the expenses.csv sitting next to this script,
# no matter which folder the program is run from.
FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses.csv")
REPORT_FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "spending_report.txt")

WEEKLY_BUDGET = 5000  # PKR
CATEGORIES = ["Food", "Transport", "Study", "Entertainment", "Other"]


def load_expenses(filename):
    # If the file does not exist, there are no expenses yet.
    if not os.path.exists(filename):
        return []
    expenses = []
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # CSV stores everything as text, so convert amount to a number.
            row["amount"] = float(row["amount"])
            expenses.append(row)
    return expenses


def add_expense(filename):
    # Keep asking until the date is in the correct YYYY-MM-DD format.
    while True:
        date = input("Date (YYYY-MM-DD): ")
        try:
            datetime.date.fromisoformat(date)
            break  # the date is valid, leave the loop
        except ValueError:
            print("That is not a valid date. Please use YYYY-MM-DD.")

    # Keep asking until the category is one of the allowed ones.
    while True:
        category = input("Category (Food/Transport/Study/Entertainment/Other): ").capitalize()
        if category in CATEGORIES:
            break
        print("Please choose one of:", ", ".join(CATEGORIES))

    # Keep asking until the amount is a valid number.
    while True:
        try:
            amount = float(input("Amount (PKR): "))
            break  # the amount is valid, leave the loop
        except ValueError:
            print("That is not a valid number. Please enter something like 450 or 249.50.")

    description = input("Description: ")

    # Append means: add one row at the end, keep everything already there.
    with open(filename, "a", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["date", "category", "amount", "description"])
        writer.writerow({"date": date, "category": category,
                         "amount": amount, "description": description})
    print("Expense added!")


def calculate_summary(expenses):
    # Work everything out and return it in one dictionary.
    # No printing here - that makes this function easy to test.
    total = 0
    by_category = {}

    for expense in expenses:
        total = total + expense["amount"]
        category = expense["category"]
        if category in by_category:
            by_category[category] = by_category[category] + expense["amount"]
        else:
            by_category[category] = expense["amount"]

    # Find the category with the biggest total.
    highest_category = None
    highest_amount = 0
    for category in by_category:
        if by_category[category] > highest_amount:
            highest_amount = by_category[category]
            highest_category = category

    # Spending in the most recent 7 days found in the data:
    # take the newest date, then sum everything within 7 days of it.
    recent_total = 0
    if expenses:
        newest = max(datetime.date.fromisoformat(e["date"]) for e in expenses)
        week_start = newest - datetime.timedelta(days=6)
        for expense in expenses:
            when = datetime.date.fromisoformat(expense["date"])
            if when >= week_start:
                recent_total = recent_total + expense["amount"]

    within_budget = recent_total <= WEEKLY_BUDGET

    return {
        "total": total,
        "by_category": by_category,
        "highest_category": highest_category,
        "recent_total": recent_total,
        "within_budget": within_budget,
    }


def create_report(expenses, report_filename):
    summary = calculate_summary(expenses)

    # "w" means write from scratch: the old report is replaced each time.
    with open(report_filename, "w") as file:
        file.write("SPENDING REPORT\n")
        file.write("===============\n")
        file.write("Total spending: PKR {:,.2f}\n".format(summary["total"]))
        for category in summary["by_category"]:
            file.write("{}: PKR {:,.2f}\n".format(
                category, summary["by_category"][category]))
        file.write("Highest category: {}\n".format(summary["highest_category"]))
        file.write("Recent 7-day spending: PKR {:,.2f}\n".format(
            summary["recent_total"]))
        if summary["within_budget"]:
            file.write("Weekly budget status: Within budget\n")
        else:
            file.write("Weekly budget status: OVER BUDGET\n")
    print("Report saved to spending_report.txt")


def show_summary(expenses):
    # Print the summary on screen. The math lives in calculate_summary;
    # this function only handles the printing.
    summary = calculate_summary(expenses)
    print()
    print("TOTAL SPENDING: PKR {:,.2f}".format(summary["total"]))
    print()
    print("BY CATEGORY")
    for category in summary["by_category"]:
        print("{}: PKR {:,.2f}".format(category, summary["by_category"][category]))
    print()
    print("Highest category:", summary["highest_category"])
    print("Recent 7-day spending: PKR {:,.2f}".format(summary["recent_total"]))
    print("Weekly budget: PKR {:,.2f}".format(WEEKLY_BUDGET))
    if summary["within_budget"]:
        print("Status: Within budget")
    else:
        print("Status: OVER BUDGET")


def main():
    options = ["View spending summary", "Add expense", "Create report", "Exit"]
    while True:
        print()
        print("SIMPLE EXPENSE TRACKER")
        print("----------------------")
        for i in range(len(options)):
            print(str(i + 1) + ". " + options[i])

        # int() crashes on text like "banana", so ask inside try/except.
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Please enter a number from 1 to 4.")
            continue

        if choice == 1:
            expenses = load_expenses(FILENAME)
            show_summary(expenses)
        elif choice == 2:
            add_expense(FILENAME)
        elif choice == 3:
            expenses = load_expenses(FILENAME)
            create_report(expenses, REPORT_FILENAME)
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    # --report mode: create the report and exit without showing the menu.
    # GitHub Actions will use this to generate the report automatically.
    if "--report" in sys.argv:
        expenses = load_expenses(FILENAME)
        create_report(expenses, REPORT_FILENAME)
    else:
        main()
