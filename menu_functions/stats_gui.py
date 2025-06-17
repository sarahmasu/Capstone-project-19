# =============Libraries=============
import tkinter as tk
from tkinter import messagebox
from tkcalendar import *

# =============GUI Section=============

# ----Statistics Section----


def stats():

    stats_win = tk.Toplevel()
    stats_win.title("Statistics")
    stats_win.config(bg="#333333")
    stats_win.geometry("250x200")
    frame = tk.Frame(stats_win, bg="#333333")

    # Reads the task.txt
    # Counts the number of tasks
    # prints the total number of tasks in the file
    # Reads the user.txt file, counts the number of users
    # prints end results

    # ---- Widgets ----
    header_lbl = tk.Label(
        frame, text="Statistics", bg="#333333", fg="#ffffff", font=("Arial", 25)
    )
    close_btn = tk.Button(
        frame,
        text="Close",
        width=15,
        font=("Arial", 12),
        command=stats_win.destroy,
        bg="#46a094",
        fg="#ffffff",
    )

    try:
        # ---- Read File ----
        with open("tasks.txt", "r") as read:
            total_tasks = len(read.readlines())
            tasks_lbl = tk.Label(
                frame,
                text=f"Total number of tasks: {total_tasks}",
                fg="#ffffff",
                bg="#333333",
                font=("Arial", 12),
            )

        with open("user.txt", "r") as read:
            total_user = len(read.readlines())
            user_lbl = tk.Label(
                frame,
                text=f"Total number of users: {total_user}",
                fg="#ffffff",
                bg="#333333",
                font=("Arial", 12),
            )

    except FileNotFoundError as error:
        messagebox.showerror(title="Error", message=f"An error occurred: {error}")

    # ---- Grid ----
    header_lbl.grid(row=0, column=0, columnspan=2, pady=10, sticky="news")
    tasks_lbl.grid(row=1, column=0, pady=5, sticky="w")
    user_lbl.grid(row=2, column=0, pady=5, sticky="w")
    close_btn.grid(row=3, column=0, columnspan=2, pady=10, sticky="we")

    frame.pack()
