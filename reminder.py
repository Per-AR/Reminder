import tkinter as tk
from tkinter import ttk
from datetime import datetime
from plyer import notification

class ReminderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Reminder App")
        self.master.configure(bg="#2E4057")  

        self.eye_exercise_interval = 30  
        self.move_around_interval = 60  
        self.drink_water_interval = 90  

        self.eye_exercise_last_notification = datetime.now()
        self.move_around_last_notification = datetime.now()
        self.drink_water_last_notification = datetime.now()

        style = ttk.Style()
        style.configure("TLabel", background="#2E4057", foreground="white")  
        style.configure("TButton", background="#4E6E98", foreground="#4E6E98", borderwidth=5, bordercolor="#000000", 
                        focusthickness=3, focuscolor="#4E6E98", borderradius=30)  
        style.configure("TEntry", fieldbackground="#34495E", foreground="teal", borderwidth=5, bordercolor="#34495E", 
                        focusthickness=3, focuscolor="#4E6E98", borderradius=30)  

        self.eye_exercise_label = ttk.Label(master, text="Eye Exercise Interval (minutes):")
        self.eye_exercise_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.eye_exercise_entry = ttk.Entry(master)
        self.eye_exercise_entry.grid(row=0, column=1, padx=5, pady=5)
        self.eye_exercise_entry.insert(tk.END, str(self.eye_exercise_interval))

        self.move_around_label = ttk.Label(master, text="Move Around Interval (minutes):")
        self.move_around_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.move_around_entry = ttk.Entry(master)
        self.move_around_entry.grid(row=1, column=1, padx=5, pady=5)
        self.move_around_entry.insert(tk.END, str(self.move_around_interval))

        self.drink_water_label = ttk.Label(master, text="Drink Water Interval (minutes):")
        self.drink_water_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.drink_water_entry = ttk.Entry(master)
        self.drink_water_entry.grid(row=2, column=1, padx=5, pady=5)
        self.drink_water_entry.insert(tk.END, str(self.drink_water_interval))

        self.set_intervals_button = ttk.Button(master, text="Set Intervals", command=self.set_intervals)
        self.set_intervals_button.grid(row=3, columnspan=2, padx=5, pady=5, sticky="we")

        self.check_reminders()

    def set_intervals(self):
        try:
            self.eye_exercise_interval = int(self.eye_exercise_entry.get())
            self.move_around_interval = int(self.move_around_entry.get())
            self.drink_water_interval = int(self.drink_water_entry.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid interval. Please enter a valid number.")
            return

    def check_reminders(self):
        now = datetime.now()

        if (now - self.eye_exercise_last_notification).seconds / 60 >= self.eye_exercise_interval:
            self.eye_exercise_last_notification = now
            notification_title = "Reminder: Eye Exercise"
            notification_text = "It's time to do some eye exercises!"
            notification.notify(title=notification_title, message=notification_text)

        if (now - self.move_around_last_notification).seconds / 60 >= self.move_around_interval:
            self.move_around_last_notification = now
            notification_title = "Reminder: Move Around"
            notification_text = "It's time to stand up and move around!"
            notification.notify(title=notification_title, message=notification_text)

        if (now - self.drink_water_last_notification).seconds / 60 >= self.drink_water_interval:
            self.drink_water_last_notification = now
            notification_title = "Reminder: Drink Water"
            notification_text = "It's time to drink some water!"
            notification.notify(title=notification_title, message=notification_text)

        self.master.after(60000, self.check_reminders) 
        
if __name__ == "__main__":
    root = tk.Tk()
    app = ReminderApp(root)
    root.mainloop()
