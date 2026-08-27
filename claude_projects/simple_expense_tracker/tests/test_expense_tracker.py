# Tests for the Simple Expense Tracker.
# All tests use their own sample data, so the real expenses.csv
# is never read or changed.

import os
import sys
import tempfile
import unittest

# The program lives one folder above this tests folder.
# Add that folder to Python's import search path so the import
# below works no matter where the tests are run from.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from expense_tracker import calculate_summary, create_report

# The same fictional rows as the handout example.
SAMPLE_EXPENSES = [
    {"date": "2026-08-20", "category": "Food", "amount": 450.0,
     "description": "Lunch"},
    {"date": "2026-08-21", "category": "Transport", "amount": 300.0,
     "description": "Ride to class"},
    {"date": "2026-08-22", "category": "Study", "amount": 1200.0,
     "description": "Programming book"},
    {"date": "2026-08-23", "category": "Food", "amount": 250.0,
     "description": "Coffee and snack"},
]


class TestCalculateSummary(unittest.TestCase):

    def test_total_spending_is_2200(self):
        summary = calculate_summary(SAMPLE_EXPENSES)
        self.assertEqual(summary["total"], 2200.0)

    def test_food_is_grouped_correctly(self):
        # Two Food rows (450 + 250) should merge into one total of 700.
        summary = calculate_summary(SAMPLE_EXPENSES)
        self.assertEqual(summary["by_category"]["Food"], 700.0)

    def test_study_is_the_highest_category(self):
        summary = calculate_summary(SAMPLE_EXPENSES)
        self.assertEqual(summary["highest_category"], "Study")

    def test_empty_list_gives_zero_totals(self):
        # No expenses should mean zeros and no crash.
        summary = calculate_summary([])
        self.assertEqual(summary["total"], 0)
        self.assertEqual(summary["by_category"], {})
        self.assertIsNone(summary["highest_category"])
        self.assertEqual(summary["recent_total"], 0)


class TestCreateReport(unittest.TestCase):

    def test_report_file_contains_total(self):
        # Write the report into a temporary file, not the real one.
        report_path = os.path.join(tempfile.gettempdir(),
                                   "test_spending_report.txt")
        create_report(SAMPLE_EXPENSES, report_path)

        self.assertTrue(os.path.exists(report_path))
        with open(report_path) as file:
            content = file.read()
        self.assertIn("2,200.00", content)

        os.remove(report_path)  # clean up the temporary file


if __name__ == "__main__":
    unittest.main()
