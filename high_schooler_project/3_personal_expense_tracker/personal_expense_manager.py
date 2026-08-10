import csv
import os
from datetime import date, datetime

HEADERS = ["ExpenseId", "Date", "Category", "Description", "Amount", "Payment Method"]

CATEGORIES = [
    "Food",
    "Transport",
    "Education",
    "Entertainment",
    "Shopping",
    "Bills",
    "Health",
    "Other",
]

PAYMENT_METHODS = ["Cash", "Card", "Online"]

FILE_PATH = os.path.join(os.path.dirname(__file__), "expense_list.csv")

MIN_DATE = date(2000, 1, 1)


def normalize_saved_date(value):
    """Convert supported saved date formats to DD-MM-YYYY."""
    value = value.strip()

    for date_format in ("%d-%m-%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, date_format).strftime("%d-%m-%Y")
        except ValueError:
            continue

    return value


def load_data():
    """Load expense rows from CSV. Return an empty list if the file is absent or empty."""
    try:
        with open(FILE_PATH, "r", newline="", encoding="utf-8") as file:
            rows = list(csv.reader(file))
    except FileNotFoundError:
        return []
    except PermissionError:
        print("The expense file cannot be read because permission was denied.")
        return []

    if not rows:
        return []

    if rows[0] == HEADERS:
        rows = rows[1:]

    # Ignore blank or incomplete rows and normalize saved values.
    expenses = []

    for row in rows:
        if not row or len(row) < 6:
            continue

        row = [str(value).strip() for value in row[:6]]
        row[1] = normalize_saved_date(row[1])
        expenses.append(row)

    return expenses


def save_data(expenses):
    """Write the current in-memory expense list to CSV."""
    try:
        with open(FILE_PATH, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)
            writer.writerows(expenses)

        print("Data saved successfully.")
        return True

    except PermissionError:
        print("The expense file cannot be written because permission was denied.")
        return False


def next_expense_id(expenses):
    """Return one more than the highest existing numeric expense ID."""
    ids = []

    for row in expenses:
        try:
            ids.append(int(row[0]))
        except (IndexError, ValueError):
            continue

    return str(max(ids, default=0) + 1)


def get_valid_date(prompt="Enter date of expense (dd-mm-yyyy): "):
    """Ask for and validate a date, returning it as DD-MM-YYYY text."""
    while True:
        value = input(prompt).strip()

        try:
            parsed_date = datetime.strptime(value, "%d-%m-%Y").date()
        except ValueError:
            print("Invalid date. Please use DD-MM-YYYY, for example 10-08-2026.")
            continue

        if parsed_date < MIN_DATE:
            print(f"Date cannot be earlier than {MIN_DATE.strftime('%d-%m-%Y')}.")
            continue

        if parsed_date > date.today():
            print(
                f"Date cannot be after today "
                f"({date.today().strftime('%d-%m-%Y')})."
            )
            continue

        return parsed_date.strftime("%d-%m-%Y")


def choose_from_list(title, options, prompt):
    """Display numbered options and return the chosen text."""
    print(title)

    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    while True:
        try:
            choice = int(input(prompt))

            if 1 <= choice <= len(options):
                return options[choice - 1]

        except ValueError:
            pass

        print(f"Invalid choice. Please enter a number from 1 to {len(options)}.")


def get_description(prompt="Description of expense: "):
    while True:
        description = input(prompt).strip()

        if description:
            return description

        print("Description cannot be empty.")


def get_amount(prompt="Enter amount: "):
    while True:
        try:
            amount = float(input(prompt))
        except ValueError:
            print("Please enter a number.")
            continue

        if amount <= 0:
            print("Amount must be greater than zero.")
            continue

        return amount


def add_expense(expenses):
    expense_id = next_expense_id(expenses)

    expense_date = get_valid_date()

    category = choose_from_list(
        "\nEXPENSE CATEGORIES",
        CATEGORIES,
        "Choose category (1-8): "
    )

    description = get_description()

    amount = get_amount()

    method = choose_from_list(
        "\nPAYMENT METHODS",
        PAYMENT_METHODS,
        "Choose payment method (1-3): "
    )

    expenses.append(
        [
            expense_id,
            expense_date,
            category,
            description,
            f"{amount:.2f}",
            method
        ]
    )

    print(f"Expense added successfully. New expense ID: {expense_id}")


def print_expense_table(rows):
    print(
        f"|{'ExpenseId':<10}|{'Date':<12}|{'Category':<15}|"
        f"{'Description':<35}|{'Amount':>12}|{'Payment':<10}|"
    )

    print("-" * 103)

    for row in rows:
        print(
            f"|{row[0]:<10}|{row[1]:<12}|{row[2]:<15}|"
            f"{row[3][:35]:<35}|{float(row[4]):>12.2f}|{row[5]:<10}|"
        )


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print_expense_table(expenses)

    total = sum(float(row[4]) for row in expenses)

    print(f"\nRecords present: {len(expenses)}")
    print(f"Total PKR: {total:.2f}")


def search_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    while True:
        print("\n1. Search by category")
        print("2. Search by description")

        try:
            search_by = int(input("Choose 1 or 2: "))
        except ValueError:
            print("Please enter 1 or 2.")
            continue

        if search_by == 1:
            category = choose_from_list(
                "\nEXPENSE CATEGORIES",
                CATEGORIES,
                "Choose category (1-8): "
            )

            matches = [row for row in expenses if row[2] == category]
            break

        if search_by == 2:
            search_text = input(
                "Enter description text to search for: "
            ).strip().lower()

            matches = [
                row for row in expenses
                if search_text in row[3].lower()
            ]
            break

        print("Please enter 1 or 2.")

    if not matches:
        print("No matching data found.")
        return

    print(f"{len(matches)} matching expense(s) found:")
    print_expense_table(matches)


def spending_summary(expenses):
    if not expenses:
        print("No expenses available for a summary.")
        return

    category_totals = {category: 0.0 for category in CATEGORIES}
    grand_total = 0.0

    for row in expenses:
        amount = float(row[4])
        grand_total += amount

        if row[2] in category_totals:
            category_totals[row[2]] += amount

    average = grand_total / len(expenses)

    highest_total = max(category_totals.values())

    highest_categories = [
        category
        for category, total in category_totals.items()
        if total == highest_total
    ]

    largest_amount = max(float(row[4]) for row in expenses)

    largest_expenses = [
        row for row in expenses
        if float(row[4]) == largest_amount
    ]

    print("SPENDING SUMMARY".center(50, "_"))

    print(f"Grand total: PKR {grand_total:.2f}")
    print(f"Total expenses: {len(expenses)}")
    print(f"Average expense: PKR {average:.2f}")

    for category in CATEGORIES:
        print(f"{category}: PKR {category_totals[category]:.2f}")

    print(f"Highest-spending category: {', '.join(highest_categories)}")

    for row in largest_expenses:
        print(
            "Largest expense: "
            f"ID {row[0]}, {row[1]}, {row[2]}, {row[3]}, "
            f"PKR {float(row[4]):.2f}, {row[5]}"
        )


def find_expense_by_id(expenses, expense_id):
    for row in expenses:
        try:
            if int(row[0]) == expense_id:
                return row
        except (IndexError, ValueError):
            continue

    return None


def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()

        if answer in ("yes", "y"):
            return True

        if answer in ("no", "n"):
            return False

        print("Please answer yes or no.")


def edit_expense(expenses):
    if not expenses:
        print("No expenses found.")
        return

    try:
        expense_id = int(
            input("Enter the expense ID you want to edit: ")
        )
    except ValueError:
        print("Expense ID must be a number.")
        return

    row = find_expense_by_id(expenses, expense_id)

    if row is None:
        print("ID not found.")
        return

    print("Current expense:")
    print_expense_table([row])

    if ask_yes_no("Change date? (yes/no): "):
        row[1] = get_valid_date()

    if ask_yes_no("Change category? (yes/no): "):
        row[2] = choose_from_list(
            "\nEXPENSE CATEGORIES",
            CATEGORIES,
            "Choose category (1-8): "
        )

    if ask_yes_no("Change description? (yes/no): "):
        row[3] = get_description()

    if ask_yes_no("Change amount? (yes/no): "):
        row[4] = f"{get_amount():.2f}"

    if ask_yes_no("Change payment method? (yes/no): "):
        row[5] = choose_from_list(
            "\nPAYMENT METHODS",
            PAYMENT_METHODS,
            "Choose payment method (1-3): "
        )

    print("Expense updated successfully.")


def delete_expense(expenses):
    if not expenses:
        print("No expenses found.")
        return False

    try:
        expense_id = int(
            input("Enter the expense ID you want to delete: ")
        )
    except ValueError:
        print("Expense ID must be a number.")
        return False

    row = find_expense_by_id(expenses, expense_id)

    if row is None:
        print("ID not found.")
        return False

    print("Expense selected for deletion:")
    print_expense_table([row])

    if ask_yes_no("Delete this expense? (yes/no): "):
        expenses.remove(row)
        print("Expense deleted.")
        return True

    print("Expense not deleted.")
    return False


def main():
    expenses = load_data()
    unsaved_changes = False

    while True:
        print(
            "\nMENU\n"
            "1. Add Expense\n"
            "2. View Expenses\n"
            "3. Search Expenses\n"
            "4. See Spending Summary\n"
            "5. Edit an Expense\n"
            "6. Delete an Expense\n"
            "7. Save Contents\n"
            "8. Exit\n"
        )

        try:
            choice = int(input("What do you want to do? "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 8.")
            continue

        if choice == 1:
            add_expense(expenses)
            unsaved_changes = True

        elif choice == 2:
            view_expenses(expenses)

        elif choice == 3:
            search_expenses(expenses)

        elif choice == 4:
            spending_summary(expenses)

        elif choice == 5:
            edit_expense(expenses)
            unsaved_changes = True

        elif choice == 6:
            if delete_expense(expenses):
                unsaved_changes = True

        elif choice == 7:
            if save_data(expenses):
                unsaved_changes = False

        elif choice == 8:
            if unsaved_changes and ask_yes_no(
                "You have unsaved changes. Save before exit? (yes/no): "
            ):
                save_data(expenses)

            print("Goodbye.")
            break

        else:
            print("Invalid input. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()


