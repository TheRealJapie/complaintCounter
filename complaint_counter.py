import tkinter as tk
from tkinter import messagebox
import os

COUNTER_FILE = "complaint_days.txt"

def read_counter():
    if os.path.isfile(COUNTER_FILE):
        with open(COUNTER_FILE, "r") as f:
            return int(f.read())
    else:
        return 0

def write_counter(value):
    with open(COUNTER_FILE, "w") as f:
        f.write(str(value))

def complaint_yes():
    write_counter(0)
    messagebox.showinfo("Counter Reset", "Days without complaints: 0")
    root.destroy()

def complaint_no():
    days = read_counter() + 1
    write_counter(days)
    messagebox.showinfo("Counter Updated", f"Days without complaints: {days}")
    root.destroy()

root = tk.Tk()
root.title("Philips Complaint Tracker")
root.geometry("400x100")

label = tk.Label(root, text="Was a Philips complaint registered today?")
label.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

yes_button = tk.Button(frame, text="Yes", width=10, command=complaint_yes)
yes_button.pack(side="left", padx=10)

no_button = tk.Button(frame, text="No", width=10, command=complaint_no)
no_button.pack(side="right", padx=10)

root.mainloop()
