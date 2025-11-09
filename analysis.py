"""
This file contains all the analysis functions for your habits.
It can answer questions like: which habit has my longest streak?
What are all my daily habits? How am I doing with my completion rates?
These functions use functional programming.
"""


from habit import Habit
from datetime import date


def get_habits(tracker):   # Get all habits from tracker
    return tracker.list_all_habits()

def list_habits_by_periodicity(tracker, periodicity):  # Get habits filtered by periodicity (daily/weekly)
    
    habits_list =  []
    for habit in tracker.habits:
        if habit.periodicity == periodicity:
            habits_list.append(habit)
    return habits_list

def current_streak(habit):  # Returns the current streak of a habit
    return habit.calculate_streak()

def longest_streak(tracker):  # Returns the longest streak of a habit
    
    if not tracker.habits:
        return None
    
    longest_habit = tracker.habits[0] 
    for habit in tracker.habits:
        if habit.calculate_streak() > longest_habit.calculate_streak():
            longest_habit = habit
    return longest_habit

def lowest_streak(tracker):  # Returns the habit with the lowest current streak

    if not tracker.habits:
        return None
    
    lowest_habit = tracker.habits[0] 
    for habit in tracker.habits:
        if habit.calculate_streak() < lowest_habit.calculate_streak():
            lowest_habit = habit
    return lowest_habit

def completion_rate(habit):  
    """ 
    Returns the completion rate percentage for a habit based on its periodicity (daily/weekly).
    """

    if not habit.completions: # Return 0 if there are no completions 
        return 0.0
    
    today = date.today() #  Calculates days since creation (adds 1 to include creation day)
    days_since_creation = (today - habit.creation_date).days + 1  

    if habit.periodicity == 'daily': # Daily habits: expected to complete once per day
        expected_completions = days_since_creation
        actual_completions = len(habit.completions)
    
    elif habit.periodicity == 'weekly': # Weekly habits: calculate complete weeks since creation
        weeks_since_creation = (days_since_creation + 6 ) // 7 # Round up to the nearest week
        expected_completions = max(1, weeks_since_creation)
        actual_completions = len(habit.completions)
    
    if expected_completions == 0: 
        return 0.0
    
    return (actual_completions / expected_completions) * 100 # Calculate completion percentage
    





