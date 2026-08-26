# Tests for the Study Deadline Checker.
# A fixed date is used so the tests give the same answer every day.

import datetime
import os
import sys
import unittest

# The program lives one folder above this tests folder.
# Add that folder to Python's import search path so the import
# below works no matter where the tests are run from.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from study_deadline_checker import sort_tasks

# The same fixed date as the handout example.
FIXED_TODAY = datetime.date(2026, 8, 22)


def make_task(due_date, completed="no"):
    # Small helper so each test can build a task in one line.
    return {"subject": "Test", "task": "Example",
            "due_date": due_date, "completed": completed}


class TestSortTasks(unittest.TestCase):

    def test_task_before_today_is_overdue(self):
        tasks = [make_task("2026-08-19")]
        overdue, upcoming, completed_count = sort_tasks(tasks, FIXED_TODAY)
        self.assertEqual(len(overdue), 1)
        self.assertEqual(len(upcoming), 0)

    def test_task_within_next_7_days_is_upcoming(self):
        tasks = [make_task("2026-08-25")]
        overdue, upcoming, completed_count = sort_tasks(tasks, FIXED_TODAY)
        self.assertEqual(len(overdue), 0)
        self.assertEqual(len(upcoming), 1)

    def test_completed_task_is_not_overdue_or_upcoming(self):
        tasks = [make_task("2026-08-19", completed="yes")]
        overdue, upcoming, completed_count = sort_tasks(tasks, FIXED_TODAY)
        self.assertEqual(len(overdue), 0)
        self.assertEqual(len(upcoming), 0)
        self.assertEqual(completed_count, 1)

    def test_empty_task_list_does_not_crash(self):
        overdue, upcoming, completed_count = sort_tasks([], FIXED_TODAY)
        self.assertEqual(overdue, [])
        self.assertEqual(upcoming, [])
        self.assertEqual(completed_count, 0)


if __name__ == "__main__":
    unittest.main()
