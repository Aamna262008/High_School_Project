# Simple Expense Tracker

A small command-line program that reads expenses from a CSV file and shows
spending totals, the highest category, and a weekly budget check.

Repository path: `claude_projects/simple_expense_tracker`

## CSV format

Expenses are stored in `expenses.csv` with four columns:

```
date,category,amount,description
2026-08-20,Food,450,Lunch
```

Dates use the YYYY-MM-DD format. Categories: Food, Transport, Study,
Entertainment, Other. All data is fictional sample data.

## How to run

```
python expense_tracker.py
```

To create only the report (no menu):

```
python expense_tracker.py --report
```

This writes `spending_report.txt`.

## How to run the tests

(Tests will be added later.)

## GitHub Actions

(To be written when the automation is added: after a push, GitHub runs the
tests and generates the spending report as a downloadable artifact.)

## What I learned

(To be written when the project is finished.)
