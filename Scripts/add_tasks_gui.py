# ====Import Libraries====
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
import Scripts.functions as fun

# =============GUI Section=============

# ----Add tasks Function----


# Request the user to assign other users tasks, the name of the task the description and due date.
# Saves the input into tasks.txt file.
def add_task(frame, check_username, today):
    # Creates second window
    """task_win = tk.Toplevel()
    task_win.title("Add Task")
    task_win.config(bg="#333333")
    frame = tk.Frame(task_win, bg="#333333")"""

    # Clear the frame first
    fun.clear_frame(frame)

    # ----Labels----
    header_lbl = tk.Label(
        frame, text="Assign Tasks", bg="#333333", fg="#46a094", font=("Arial", 18)
    )

    instr_lbl = tk.Label(
        frame,
        text="Please complete the following:",
        bg="#333333",
        fg="#ffffff",
        font=("Arial", 15),
    )

    user_lbl = tk.Label(
        frame, text="Select a user: ", bg="#333333", fg="#ffffff", font=("Arial", 12)
    )

    title_lbl = tk.Label(
        frame, text="Task title: ", bg="#333333", fg="#ffffff", font=("Arial", 12)
    )

    description_lbl = tk.Label(
        frame, text="Task description: ", fg="#ffffff", bg="#333333", font=("Arial", 12)
    )

    due_date_lbl = tk.Label(
        frame, text="Select due date: ", bg="#333333", fg="#ffffff", font=("Arial", 12)
    )

    current_date_lbl = tk.Label(
        frame, text="Current date: ", bg="#333333", fg="#ffffff", font=("Arial", 12)
    )

    current_date_lbl2 = tk.Label(
        frame,
        text=f"{today.strftime("%d %b %Y")}",
        bg="#333333",
        fg="#ffffff",
        font=("Arial", 12),
    )

    status_lbl = tk.Label(
        frame, text="Task complete: ", bg="#333333", fg="#ffffff", font=("Arial", 12)
    )

    task_complete_lbl = tk.Label(
        frame, text="No", bg="#333333", fg="#ffffff", font=("Arial", 12)
    )

    # ----Combobox----
    select_user = tk.StringVar()

    user_cmbo = ttk.Combobox(
        frame, width=25, textvariable=select_user, font=("Arial", 12)
    )

    user_cmbo["values"] = tuple(check_username)

    user_cmbo["state"] = "readonly"

    # ----Entry and Text boxes----
    task_title_txt = tk.Entry(frame, width=27, font=("Arial", 12))

    task_description_txt = tk.Text(frame, width=27, height=3, font=("Arial", 12))

    # ----Calendar Widget----
    task_due_date = Calendar(
        frame,
        selectmode="day",
        year=today.year,
        month=today.month,
        day=today.day,
        date_pattern="dd mm y",
        background="#333333",
        foreground="#ffffff",
        selectbackground="#46a094",
        selectforeground="#ffffff",
        headersbackground="#46a094",
        headersforeground="#ffffff",
    )

    # ----Buttons----
    save_task_btn = tk.Button(
        frame,
        text="Submit",
        width=15,
        font=("Arial", 12),
        command=lambda: fun.submit_tasks(
            select_user.get(),
            task_title_txt.get(),
            task_description_txt.get("1.0", "end-1c"),
            current_date_lbl2.cget("text"),
            task_due_date.selection_get().strftime("%d %b %Y"),
            task_complete_lbl.cget("text"),
        ),
        bg="#46a094",
        fg="#ffffff",
    )

    clear_btn = tk.Button(
        frame,
        text="Clear",
        width=15,
        font=("Arial", 12),
        command=lambda: fun.clear(frame),
        bg="#46a094",
        fg="#ffffff",
    )

    # ----Grid layout---

    # ++Labels++
    header_lbl.grid(row=0, column=0, columnspan=3, pady=25, sticky="news")
    instr_lbl.grid(row=1, column=0, columnspan=3, pady=5, sticky="w")

    user_lbl.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    title_lbl.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    description_lbl.grid(row=4, column=0, padx=5, pady=5, sticky="w")

    due_date_lbl.grid(row=5, column=0, padx=5, pady=5, sticky="w")

    current_date_lbl.grid(row=6, column=0, padx=5, pady=5, sticky="w")
    current_date_lbl2.grid(row=6, column=1, padx=5, pady=5, sticky="w")

    status_lbl.grid(row=7, column=0, padx=5, pady=5, sticky="w")
    task_complete_lbl.grid(row=7, column=1, padx=5, pady=5, sticky="w")

    # ++Text and Entry++
    task_title_txt.grid(row=3, column=1, padx=5, pady=5, sticky="w")
    task_description_txt.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    # ++Calendar++
    task_due_date.grid(row=5, column=1, padx=5, pady=5, sticky="w")

    # ++Combobox++
    user_cmbo.grid(row=2, column=1, pady=5, padx=5, sticky="w")

    # ++buttons++
    save_task_btn.grid(row=8, column=0, pady=5, sticky="e")
    clear_btn.grid(row=8, column=1, pady=5, sticky="w")

    frame.pack()
