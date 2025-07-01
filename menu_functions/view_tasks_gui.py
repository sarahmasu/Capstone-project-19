# ====Import Libraries====
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
import os.path
import menu_functions.functions as fun

# =============GUI Section=============

# ----View tasks Section----


def view_tasks(frame, username, menu, current_user, task_num_list, check_username, today):
    '''view_tasks_win = tk.Toplevel()
    view_tasks_win.config(bg="#333333")
    view_tasks_win.resizable(True, True)
    frame = tk.Frame(view_tasks_win, bg="#333333")'''

    # Clear the frame first
    fun.clear_frame(frame)

    txt_bx = tk.Text(frame, width=48, height=25, wrap="word", font=("Arial", 11))
    # txt_bx.config(state=tk.DISABLED)  # Prevents users from editing the text box.

    vert_scroll = ttk.Scrollbar(frame, orient="vertical", command=txt_bx.yview)
    horizon_scroll = ttk.Scrollbar(frame, orient="horizontal", command=txt_bx.xview)

    if menu == "View all tasks":

        '''view_tasks_win.title("View All Tasks")'''

        # ---- Widgets ----
        info_lbl = tk.Label(
            frame,
            text="List of all the tasks",
            bg="#333333",
            fg="#ffffff",
            font=("Arial", 20),
        )

        gen_report_btn = tk.Button(
        frame,
        text="Generate report",
        width=15,
        font=("Arial", 12),
        bg="#46a094",
        fg="#ffffff",
        command= lambda: fun.generate_report(check_username, txt_bx)
    )

        # ---- Read File ----

        # Read the task.txt file to display all the task and which user is assign to it
        file_size = os.path.getsize("tasks.txt")

        try:
            if file_size != 0:
                with open("tasks.txt", "r", encoding="utf-8") as read_all_tasks:
                    lines = read_all_tasks.readlines()

                    # Iterate through task.txt file
                    for count, line in enumerate(lines, start=1):

                        # Split the lines where there is a comma and a space
                        split_lines = line.split(",")

                        # The variables will be stored in assigned_user, title, description, assigned_date,
                        # due_date, and task_complete
                        assigned_user = split_lines[0]
                        title = split_lines[1]
                        description = split_lines[2]
                        assigned_date = split_lines[3]
                        due_date = split_lines[4]
                        complete_task = split_lines[5]

                        fun.display_tasks(
                            txt_bx,
                            count,
                            title,
                            assigned_user,
                            assigned_date,
                            due_date,
                            complete_task,
                            description,
                        )
            else:
                messagebox.showwarning(
                    title="Warning", message="File empty. Ask admin to populate file."
                )
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="File not found!")

        # ---- Grid Layout ----
        info_lbl.grid(row=0, column=0, columnspan=4, pady=10, sticky="ew")

        txt_bx.grid(row=1, column=2, rowspan=8, columnspan=2, sticky="ew")
        vert_scroll.grid(row=1, column=4, rowspan=8, sticky="ns")
        horizon_scroll.grid(row=9, column=2, columnspan=2, sticky="ew")
        
        gen_report_btn.grid(row=10, column=2, columnspan=2, pady=10, sticky="we")

        # ---- Scrollbar ----
        txt_bx["yscrollcommand"] = vert_scroll.set
        txt_bx["xscrollcommand"] = horizon_scroll.set

    elif menu == "View my tasks":

        '''view_tasks_win.title("My Tasks")'''
        current_user.clear()
        task_num_list.clear()

        try:

            # Read the task.txt file
            with open("tasks.txt", "r", encoding="utf-8") as read_my_tasks:
                lines = read_my_tasks.readlines()

                # Iterate through task.txt file
                for count, line in enumerate(lines, start=1):
                    # Split the lines where there is a comma and a space
                    split_lines = line.strip().split(",")

                    # Check if user is assigned a task
                    if username in split_lines[0]:

                        # The variables will be stored in my_username, my_title, my_description,
                        # my_assigned_date, my_due_date, and my_complete_task
                        my_username = split_lines[0]
                        my_title = split_lines[1]
                        my_description = split_lines[2]
                        my_assigned_date = split_lines[3]
                        my_due_date = split_lines[4]
                        my_complete_task = split_lines[5]

                        fun.display_tasks(
                            txt_bx,
                            count,
                            my_title,
                            my_username,
                            my_assigned_date,
                            my_due_date,
                            my_complete_task,
                            my_description,
                        )

                        # Add key-pair values to a list
                        current_user.append(
                            (
                                {
                                    "No": f"{count}",
                                    "username": f"{my_username}",
                                    "title": f"{my_title}",
                                    "description": f"{my_description}",
                                    "assigned date": f"{my_assigned_date}",
                                    "due date": f"{my_due_date}",
                                    "complete task": f"{my_complete_task}",
                                }
                            )
                        )

        except FileNotFoundError:
            messagebox.showerror(title="Error", message=f"File not found!")

        # ---- Widgets ----
        #    ++Labels++
        info_lbl = tk.Label(
            frame,
            text=f"List of {username}'s tasks",
            bg="#333333",
            fg="#ffffff",
            font=("Arial", 20),
        )

        task_num_lbl = tk.Label(
            frame,
            text="Select task number:",
            bg="#333333",
            fg="#ffffff",
            font=("Arial", 12),
        )

        chg_title_lbl = tk.Label(
            frame,
            text="Change task title:",
            bg="#333333",
            fg="#ffffff",
            font=("Arial", 12),
        )

        chg_status_lbl = tk.Label(
            frame,
            text="Change task status:",
            bg="#333333",
            fg="#ffffff",
            font=("Arial", 12),
        )

        chg_user_lbl = tk.Label(
            frame,
            text="Change assigned user:",
            bg="#333333",
            fg="#ffffff",
            font=("Arial", 12),
        )

        chg_due_date_lbl = tk.Label(
            frame,
            text="Change due date:",
            bg="#333333",
            fg="#ffffff",
            font=("Arial", 12),
        )

        chg_descript_lbl = tk.Label(
            frame,
            text="Change task description:",
            bg="#333333",
            fg="#ffffff",
            font=("Arial", 12),
        )

        #   ++Text and entry++
        chg_status = tk.Entry(frame, width=27, font=("Arial", 12))
        chg_descript = tk.Text(
            frame, width=27, height=3, font=("Arial", 12), wrap=tk.WORD
        )
        chg_title = tk.Text(frame, width=27, height=2, font=("Arial", 12), wrap=tk.WORD)

        #     ++Calendar++
        chg_due_date_cal = Calendar(
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

        #     ++Combo boxes++
        select_task = tk.StringVar()
        select_user = tk.StringVar()
        #  Tasks
        chg_task_num_cmbo = ttk.Combobox(
            frame,
            width=25,
            textvariable=select_task,
            font=("Arial", 12),
        )

        for task_num in current_user:
            task_num_list.append(task_num["No"])

        chg_task_num_cmbo["values"] = tuple(task_num_list)

        chg_task_num_cmbo["state"] = "readonly"

        # Users
        chg_user_cmbo = ttk.Combobox(
            frame,
            width=25,
            textvariable=select_user,
            font=("Arial", 12),
        )

        chg_user_cmbo["values"] = tuple(check_username)

        chg_user_cmbo["state"] = "readonly"

        # ++Buttons++
        update_btn = tk.Button(
            frame,
            text="Update",
            width=15,
            font=("Arial", 12),
            bg="#46a094",
            fg="#ffffff",
            command=lambda: fun.update_task(
                txt_bx,
                username,
                chg_task_num_cmbo,
                chg_title,
                chg_user_cmbo,
                chg_descript,
                chg_status,
                chg_due_date_cal,
                current_user,
            ),
        )

        clear_btn = tk.Button(
            frame,
            text="Clear",
            width=15,
            font=("Arial", 12),
            bg="#46a094",
            fg='#ffffff',
            command=lambda:fun.clear(frame)
        )

        # ---- Bindings ----
        chg_task_num_cmbo.bind(
            "<<ComboboxSelected>>",
            lambda event: fun.search_list_event(
                event,
                frame,
                chg_task_num_cmbo,
                chg_title,
                chg_user_cmbo,
                chg_descript,
                chg_status,
                chg_due_date_cal,
                txt_bx,
                current_user
            ),
        )

        # ---- Scrollbar ----
        txt_bx["yscrollcommand"] = vert_scroll.set
        txt_bx["xscrollcommand"] = horizon_scroll.set

        # ---- Grid layout ----

        info_lbl.grid(row=0, column=0, columnspan=4, pady=10, sticky="ew")

        task_num_lbl.grid(row=1, column=0, pady=5, padx=5, sticky="w")
        chg_user_lbl.grid(row=2, column=0, pady=5, padx=5, sticky="w")
        chg_title_lbl.grid(row=3, column=0, pady=5, padx=5, sticky="w")
        chg_descript_lbl.grid(row=4, column=0, pady=5, padx=5, sticky="w")
        chg_status_lbl.grid(row=5, column=0, pady=5, padx=5, sticky="w")
        chg_due_date_lbl.grid(row=6, column=0, pady=5, padx=5, sticky="w")

        chg_task_num_cmbo.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        chg_user_cmbo.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        chg_title.grid(row=3, column=1, pady=5, padx=5, sticky="w")
        chg_descript.grid(row=4, column=1, pady=5, padx=5, sticky="w")
        chg_status.grid(row=5, column=1, pady=5, padx=5, sticky="w")
        chg_due_date_cal.grid(row=6, column=1, pady=5, padx=5, sticky="w")

        txt_bx.grid(row=1, column=2, rowspan=8, columnspan=2, sticky="ew")
        vert_scroll.grid(row=1, column=4, rowspan=6, sticky="ns")
        horizon_scroll.grid(row=8, column=2, columnspan=2, sticky="ew")

        update_btn.grid(row=9, column=2, pady=10, sticky="ew")
        clear_btn.grid(row=9, column=3, pady=10, sticky="ew")

    frame.pack()
