"""
This is the main file that runs the whole habit tracker app.
It creates the menu system you interact with and connects everything together.
When you run the program, this is what starts and keeps running until you quit.
"""


from habit_tracker import HabitTracker
import analysis
import os

class HabitTrackerCLI:
    def __init__(self):
        self.tracker = HabitTracker()
        self.data_file = 'habits.json'
    
    def display_main_menu(self):
        print("\n" + "="*40)
        print("      HABIT TRACKER - MAIN MENU")
        print("="*40)
        print("1. Start (Load Data)")
        print("2. Add habit")
        print("3. Remove habit") 
        print("4. Complete habit")
        print("5. View habit")
        print("6. List all habits")
        print("7. List habits by periodicity")
        print("8. View analysis")
        print("9. Load test data")
        print("10. Exit")
        print("="*40)

    def display_analysis_menu(self):
        print("\n--- ANALYSIS MENU ---")
        print("a. View current streak for a habit")
        print("b. View longest streak")
        print("c. View lowest streak") 
        print("d. Back to main menu")
    
    def start(self):
        self.tracker.load_file(self.data_file)
        print(f"Data loaded from {self.data_file}")

    def load_test_data(self):   # Load test data for demonstration
        if not os.path.exists("test_data.json"):
            print("Error: test_data.json file not found.")

        else:   
            self.tracker.load_file("test_data.json")
            print("Test data loaded successfully!")
            print("You now have 5 sample habits to test the analysis features.")

    def add_habit(self):
        print("\n--- ADD NEW HABIT ---")
        name = input("Enter habit name: ")
        periodicity = input("Enter periodicity (daily/weekly): ").lower()

        if periodicity not in ['daily', 'weekly']:
            print("Error: Periodicity must be 'daily' or 'weekly'.")
            return
        
        self.tracker.insert_habit(name, periodicity)
        self.tracker.save_file(self.data_file)

    def remove_habit(self):
        print("\n--- REMOVE HABIT ---")
        self.list_all_habits()

        try:
            habit_id = int(input("Enter the ID of the habit to remove: "))
            self.tracker.delete_habit(habit_id)
            self.tracker.save_file(self.data_file)
        except ValueError:
            print("Error: Please enter a valid number.")

    def complete_habit(self):
        print("\n--- COMPLETE HABIT ---")
        self.list_all_habits()

        try:
            habit_id = int(input("Enter the ID of the habit to complete: "))
            habit = self.tracker.get_habit_by_id(habit_id)
            if habit:
                habit.complete_habit()
                self.tracker.save_file(self.data_file)
            else: 
                print("Error: Habit not found.")
        except ValueError:
            print("Error: Please enter a valid number.")

    def view_habit(self):
        print("\n--- VIEW HABIT ---")
        self.list_all_habits()

        try:
            habit_id = int(input("Enter the ID of the habit to view: "))
            habit = self.tracker.get_habit_by_id(habit_id)
            if habit:
                print(f"\nHabit Details:")
                print(f"ID: {habit.id}")
                print(f"Name: {habit.name}")
                print(f"Periodicity: {habit.periodicity}")
                print(f"Creation Date: {habit.creation_date}")
                print(f"Current Streak: {analysis.current_streak(habit)}")
                print(f"Completion Rate: {analysis.completion_rate(habit):.1f}%")
                print(f"Completions: {len(habit.completions)}")
            else:
                print("Sorry! Habit not found.")
        except ValueError:
            print("Error: Please enter a valid number")

    def list_all_habits(self):
        habits =  analysis.get_habits(self.tracker)

        if not habits:
            print("Sorry! No habits found.")
            return
        
        print("\n--- ALL HABITS ---")
        for habit in habits:
            streak = analysis.current_streak(habit)
            rate = analysis.completion_rate(habit)
            print(f"ID: {habit.id} | Name: {habit.name} | Periodicity: {habit.periodicity} | Streak: {streak}")

    def list_habits_by_periodicity(self):
        print("\n--- FILTER BY PERIODICITY ---")
        periodicity = input("Enter periodicity to filter by (daily/weekly): ").lower()

        if periodicity not in ['daily', 'weekly']:
            print("Error: Periodicity must be 'daily' or 'weekly'.")
            return
        
        habits = analysis.list_habits_by_periodicity(self.tracker, periodicity)

        if not habits:
            print(f"No {periodicity} habits found.")
            return
        
        print(f"\n--- {periodicity.upper()} HABITS ---")
        for habit in habits:
            streak = analysis.current_streak(habit)
            rate = analysis.completion_rate(habit)
            print(f"ID: {habit.id} | Name: {habit.name} | Streak: {streak}")

    
    def analysis_menu(self):
        while True:
            self.display_analysis_menu()
            choice = input("Select an option (a-d): ").lower()

            if choice == 'a':
                self.view_current_streak()
            elif choice == 'b':
                self.view_longest_streak()
            elif choice == 'c':
                self.view_lowest_streak() 
            elif choice == 'd':
                break
            else:
                print("Invalid option. Please choose a, b, c or d.")

    def view_current_streak(self):
        self.list_all_habits()

        try:
            habit_id = int(input("Enter habit ID: "))
            habit = self.tracker.get_habit_by_id(habit_id)
            if habit:
                streak = analysis.current_streak(habit)  
                print(f"Current streak for '{habit.name}': {streak}")
            else:
                print("Sorry! Habit not found")
        except ValueError:
            print("Error: Please enter a valid number")

    def view_longest_streak(self):
        habit = analysis.longest_streak(self.tracker)

        if habit:
            streak = analysis.current_streak(habit)
            print(f"Longest streak is for '{habit.name}' with a streak of {streak}.")
        else:
            print("Sorry! No habits found.")

    def view_lowest_streak(self):  
        habit = analysis.lowest_streak(self.tracker)

        if habit:
            streak = analysis.current_streak(habit)
            print(f"Lowest streak is for '{habit.name}' with a streak of {streak}.")
        else:
            print("Sorry! No habits found.")

    def run(self):
        print("Welcome to the Habit Tracking Application!")

        self.start()

        while True:
            self.display_main_menu()
            choice = input("Select an option (1-10): ")

            if choice == '1':
                self.start()
            elif choice == '2':
                self.add_habit()
            elif choice == '3':
                self.remove_habit()
            elif choice == '4':
                self.complete_habit()
            elif choice == '5':
                self.view_habit()
            elif choice == '6':
                self.list_all_habits()
            elif choice == '7':
                self.list_habits_by_periodicity()
            elif choice == '8':
                self.analysis_menu()
            elif choice == '9':
                self.load_test_data()
            elif choice == '10':
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid option. Please choose a number between 1 and 10.")

if __name__ == "__main__":
    app = HabitTrackerCLI()
    app.run()


        
        
        
        


        

    


              

    

        
        


        

    


              

    
