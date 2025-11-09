# Habit Tracker App

This project was created for the course **Object-Oriented and Functional Programming with Python**.  
It’s a simple command-line application that allows users to create, track and analyse daily and weekly habits.

# Project Description

The program helps users build good habits by tracking their progress over time.  
You can add new habits, mark them as completed, delete them and see some basic statistics about progress.  

All data is saved in a local JSON file so that you can close the program and continue later.

The project follows an object-oriented structure with two main classes and one module for functional analysis.

# Structure

├── main.py # Main menu and menu interface (CLI) 

├── habit.py # Habit class 

├── habit_tracker.py # HabitTracker class (manages all habits and file operations)

├── analysis.py # Functional module for habit analysis

├── habits.json # Data file automatically created by the program

├── test_data.json # Sample data with 5 habits for testing

└── test_habit_tracker_app.py

# Main Features

- Create and delete habits
- Mark habits as completed (daily or weekly)
- Track current streaks
- View completion rates
- Analyze your habits with various statistics
- Data automatically saves to JSON files

# Analysis Features

- Current streak - See how many consecutive days/weeks you've maintained a habit
- Longest streak - Find which habit has your best streak
- Lowest streak - Identify habits you're struggling with
- Filter by periodicity - See only daily or weekly habits

# Prerequisites
- Python 3.7 or later

# Installation
Download all project files to the same folder:
   - 'main.py'
   - 'habit.py'
   - 'habit_tracker.py'
   - 'analysis.py'
   - 'test_data.json' (optional)
   - 'test_habit_tracker_app.py'

# Running the Application
Run the tracker by typing this command in your terminal:

python main.py

# How to use 

When you run the program, you'll see a menu with these options:

1. Start - Load your saved habits from file
2. Add habit - Create a new daily or weekly habit
3. Remove habit - Delete a habit by ID
4. Complete habit - Mark a habit as done for today/this week
5. View habit - See details and stats for a specific habit
6. List all habits - View all your habits with current streaks
7. List habits by periodicity - Filter by daily or weekly
8. View analysis - Access analysis menu for streaks and statistics
9. Load test data - Try the app with 5 sample habits
10. Exit - Quit the application

When you close the program, it automatically saves your data in habits.json.


# Example Usage

- Try with Sample Data First:

python main.py

Choose option 9 to load test data

Choose option 8 for analysis menu

Select options a, b, or c to explore different analyses

- Create Your Own Habit:

Run the program

Choose option 2 to add a habit

Enter name (for example: "Read book")

Enter periodicity ("daily" or "weekly")

Use option 4 to mark it as completed

# Unit Tests

Basic functionality is covered by simple unit tests using Python’s built-in unittests. These tests check that a new habit can be created and deleted correctly and that the streak calculation works as expected.

To run them yourself, just open a terminal in the project folder and type:

python -m unittest test_habit_tracker_app.py

# Technical Details

- Data Storage: JSON files (no database required)
- Programming: Object-oriented (classes) + Functional (analysis)
- Dependencies: Python 3.7 or later
- Periodicities Supported: Daily and weekly

# Notes

- Your habits are automatically saved to habits.json
- Streaks count consecutive periods without breaks
- The app uses ISO date format (YYYY-MM-DD) for consistency
- Test data includes 5 sample habits
- Test data contains old completion dates, so the current streaks appear as 0. This is expected behaviour because the function calculates consecutive completions up to the current date


# Conclusion

It’s a simple but useful project that helped me understand how to combine classes and functions in Python.  

The app is small but it includes the main concepts from the course: object-oriented design, functional programming and basic file handling.

