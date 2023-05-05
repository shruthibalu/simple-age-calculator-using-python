import tkinter as tk
from datetime import date

# calculate age based on birthdate and current date
def calculate_age():
    birthdate = birthdate_entry.get()
    birthdate = date.fromisoformat(birthdate)
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    age_label.config(text=f"Age: {age}")

# create GUI window
window = tk.Tk()
window.title("Age Calculator")

# create birthdate entry field
birthdate_label = tk.Label(window, text="Enter birthdate (YYYY-MM-DD):")
birthdate_label.pack()
birthdate_entry = tk.Entry(window)
birthdate_entry.pack()

# create button to calculate age
calculate_button = tk.Button(window, text="Calculate Age", command=calculate_age)
calculate_button.pack()

# create label to display age
age_label = tk.Label(window, text="")
age_label.pack()

# start the main loop
window.mainloop()
