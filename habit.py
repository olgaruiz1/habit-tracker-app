"""
This file defines what a habit is and how it behaves.
The Habit class keeps track of things like when the habit was created,
how often it should be done and when it was actually completed.
It also figures out how long your current streak is for each habit.
"""

from datetime import date, timedelta 
# Date to get current dates and timedelta to subtract days/weeks

class Habit:

    """
    Represents a habit that the user wants to track
    Attributes: 
    - id: int, unique identifier of the habit
    - name: str, name of the habit
    - periodicity: str, frequency of the habit ('daily', 'weekly')
    - creation_date: date, date when the habit was created
    - completions: List[str], dates (ISO format) of each time the habit was completed
    """

    def __init__(self, id, name, periodicity, creation_date=None, completions=None):
        # The constructor: runs automatically when you create a habit
        # self: the habit instance being created

        self.id = id
        self.name = name
        self.periodicity = periodicity 

        if creation_date is None:   # If no date is provided, uses today's date
            self.creation_date = date.today()
        else:
            self.creation_date = creation_date

        if completions is None:   # If no completions list is provided, starts empty
            self.completions = []
        else: 
            self.completions = completions

    def complete_habit(self):

        """
        Marks the habit as completed:
        - If 'daily', adds today's date.
        - If 'weekly', adds the current week's Monday date. 
        Prevents duplicates if already marked today/this week.
        """

        today = date.today()   # Gets today's date, storing it in the variable today

        if self.periodicity == 'daily':

            today_str = today.isoformat()

            if today_str in self.completions:   # If today's date is already in completions, doesn't add it
                print("Today's habit already completed.")
            else:   # If not present, adds it
                self.completions.append(today_str)
                print(f"Habit '{self.name}' marked as completed for today!")
        
        elif self.periodicity == 'weekly':
       
            year_week = f"{today.year}-W{today.isocalendar()[1]}"   # Gets current year and week in 'YYYY-Www' format (for example, '2023-W14' for week 14 of 2023)
    
            if year_week in self.completions:   # If current week is already in completions, doesn't add it
                print("This week's habit already completed.")
            else:   # If not present, adds it
                self.completions.append(year_week)    
                print(f"Habit '{self.name}' marked as completed for this week!")
        
        else:
            print("Invalid periodicity. Use 'daily' or 'weekly', please.")

    def calculate_streak(self):

        """
        Calculates the current (consecutive) streak of the habit:
        - For daily: counts back from today until a break is found
        - For weekly: counts back from current week until a break is found
        Returns the streak count as an integer.
        """

        if not self.completions:   # If there are no completions, streak is 0
            return 0
        
        streak = 0   # Streak counter
        today = date.today()   # Today's date
        
        if self.periodicity == 'daily':
            current_date = today
            while True:   # Count consecutive days backwards from today
                date_str = current_date.isoformat()   # Converts current date to ISO text
                if date_str in self.completions:   # If current date is in completions
                    streak += 1   # Increase streak by 1
                    current_date = current_date - timedelta(days=1)   # Subtract one day from current date
                
                else:
                    break   # Breaks the loop when it finds a day not completed
        
        elif self.periodicity == 'weekly':
            current_date = today
            
            while True:   # Count consecutive weeks backwards from current week
                year_week = f"{current_date.year}-W{current_date.isocalendar()[1]}"   # Gets current year and week in 'YYYY-Www' format

                if year_week in self.completions:
                    streak += 1
                    current_date = current_date - timedelta(weeks=1)   # Subtract one week from current date
                
                else:
                    break
        
        return streak   

            
