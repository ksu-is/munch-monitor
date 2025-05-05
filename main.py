import tkinter as tk
from tkinter import simpledialog, messagebox
import threading
import time

# reminder to log meals in 3 hour spans
REMINDER_INTERVAL = 3 * 60 * 60

# main App Class
class MealTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Munch Monitor 🍽️")
        self.root.geometry("300x300")

        # prompt for user input
        goal = simpledialog.askstring("Daily Calorie Goal", "Enter your daily calorie goal:")
        try:
            self.calorie_goal = int(goal)
        except (TypeError, ValueError):
            messagebox.showerror("Invalid Input", "Using default goal of 1800 calories.")
        self.calorie_goal = 1800  # default if user does not provide calorie goal input
        self.total_calories = 0
        self.meals = []

        # title
        tk.Label(root, text="Munch Monitor 🍽️", font=("Helvetica", 16, "bold")).pack(pady=10)

    def setup_ui(self):
        # add your basic labels and buttons here
        tk.Label(self.root, text="Munch Monitor").pack()
        tk.Button(self.root, text="Log a Meal 🍱", command=self.log_meal).pack()
        tk.Button(self.root, text="View Logged Meals 📋", command=self.view_meals).pack()

    # start the reminder thread
        threading.Thread(target=self.reminder_loop, daemon=True).start()

    def get_status_text(self):
        return f"Calories: {self.total_calories} / {self.calorie_goal}"

    def log_meal(self):
        # function for logging a meal goes here
        meal_name = simpledialog.askstring("Meal Name", "Enter the meal or food item:")
        if not meal_name:
            return
        try:
            calories = int(simpledialog.askstring("Calories", f"How many calories in '{meal_name}'?"))
        except (TypeError, ValueError):
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return
            
    self.total_calories += calories
        self.meals.append((meal_name, calories))
        self.status_label.config(text=self.get_status_text())
    
    if self.total_calories >= self.calorie_goal:
        messagebox.showinfo("Goal Reached", "🎉 You've reached your daily calorie goal!")

    def view_meals(self):
        # function for viewing meals goes here
        if not self.meals:
            messagebox.showinfo("Meals Logged", "No meals logged yet.")
            return
        meal_text = "\n".join([f"{name} - {cal} cal" for name, cal in self.meals])
        messagebox.showinfo("Meals Logged Today ☑️", meal_text)


    def reminder_loop(self):
        # function for background reminders goes here
        while True:
            time.sleep(REMINDER_INTERVAL)
            self.send_reminder()

    def send_reminder(self):
        messagebox.showinfo("Munch Monitor Reminder", "⏰ Don't forget to log your meals!")

# launch the app
if __name__ == "__main__":
    root = tk.Tk()
    app = MealTrackerApp(root)
    root.mainloop()
