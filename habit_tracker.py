"""
This file manages all your habits together, like a collection.
It handles saving your habits to a file so you don't lose them,
loading them back when you restart the app and basic operations
like adding new habits or deleting old ones.
"""


import json
from datetime import date
from habit import Habit

class HabitTracker:
    """
    The main controller that manages all habits in the app
    Attributes:
    - habits: list of Habit objects being tracked
    """

    def __init__(self):
        self.habits = []   # List of Habit objects

    def insert_habit(self, name, periodicity):   # Creates a new habit and adds it to the tracker

        if self.habits:
            new_id = max(habit.id for habit in self.habits) + 1   # Finds the highest existing ID and increments it by 1
        else:
            new_id = 1

        new_habit = Habit(new_id, name, periodicity)   
        self.habits.append(new_habit)   # Adds the new habit to the list
        print(f"Habit '{name}' added with ID {new_id}.") 
        return new_habit 
   
    def delete_habit(self, habit_id):   # Deletes a habit by its ID

        habit = self.get_habit_by_id(habit_id)   # Find the habit by ID
        if habit:
            self.habits.remove(habit)   # Remove the habit from the list
            print(f"Habit with ID {habit_id} deleted.")
            return True
        print(f"Habit with ID {habit_id} not found.") 
        return False
    
    def get_habit_by_id(self, habit_id):   # Finds and returns a habit by its ID
        for habit in self.habits:
            if habit.id == habit_id:
                return habit
        return None
    
    def get_habit_by_name(self, name):   # Finds and returns a habit by its name
        for habit in self.habits:
            if habit.name.lower() == name.lower():
                return habit
        return None
    
    def save_file(self, filename):   # Saves all habits to a JSON file
        habits_data = []
        for habit in self.habits:
            habit_dict = {'id': habit.id, 'name': habit.name, 'periodicity': habit.periodicity, 'creation_date': habit.creation_date.isoformat(), 'completions': habit.completions}
            habits_data.append(habit_dict) 

        try:
            file = open(filename, 'w')   # Opens the file to write
            json.dump({'habits': habits_data}, file, indent=2)
            file.close()   # Close the file after writing
            print(f"Habits saved to {filename}.")
        
        except Exception:   # Catches any exception that occurs during file operations
            print("Error saving habits to file.")
        
    def load_file(self, filename):   # Loads habits from a JSON file
        try:
            file = open(filename, 'r')  # Opens the file to read
            data = json.load(file)
            file.close()  # Closes the file after reading

            self.habits = []  # Temporary list to hold loaded habits

            for habit_data in data.get('habits', []):
                creation_date = date.fromisoformat(habit_data['creation_date']) 
                habit = Habit(habit_data['id'], habit_data['name'], habit_data['periodicity'], creation_date, habit_data['completions']) 
                self.habits.append(habit)  # Add the loaded habit to the list            

        except FileNotFoundError:
            self.habits = []   # If file not found, start with an empty list
        
        except Exception:   
            print("Error loading habits from file.")
            self.habits = []

    def list_all_habits(self):   # Returns a list of all habits
        return self.habits
    

        

    




