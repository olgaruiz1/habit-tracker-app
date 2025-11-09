"""
Some small tests I made to check if my Habit Tracker works properly.

I wanted to test the main parts only: creating habits, calculating streaks
and deleting habits. The idea was just to see if it behaves as expected.
"""

import unittest
from datetime import date, timedelta
from habit import Habit
from habit_tracker import HabitTracker

class HabitTests(unittest.TestCase):

    def test_create_habit(self): # Checks a habit is created and is stored in the tracker
        tracker = HabitTracker()
        habit = tracker.insert_habit("Read book", "daily")

        self.assertEqual(len(tracker.habits), 1)
        self.assertEqual(habit.name, "Read book")

    def test_streak_calculation(self): # Tries 3 days in a row to see if streak works
        habit = Habit(1, "Exercise", "daily")
        today = date.today()

        habit.completions = [(today - timedelta(days=2)).isoformat(),
            (today - timedelta(days=1)).isoformat(),
            today.isoformat()]

        self.assertEqual(habit.calculate_streak(), 3)

    def test_no_streak_for_new_habit(self): # A new habit should have streak = 0
        habit = Habit(1, "New habit", "daily")
        self.assertEqual(habit.calculate_streak(), 0)

    def test_delete_habit(self): # Makes sure deleting a habit actually removes it
        tracker = HabitTracker()
        habit = tracker.insert_habit("Test habit", "daily")
        tracker.delete_habit(habit.id)
        self.assertEqual(len(tracker.habits), 0) # Checks that the list is empty after deleting the habit


if __name__ == "__main__":  # Run the tests only when this file is executed directly
    unittest.main()
