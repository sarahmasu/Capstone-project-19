# ====Import Libraries====
from datetime import date
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
import os.path

# ====Dictionaries & Lists====

check_username = []
check_passwd = []
current_user = []
task_num_list = []
user = {}

today = date.today()

# =============GUI Section=============

# ----Login Section----


def login(username, passwd):
    # if the username and the password is correct, proceed.
    if username in user and passwd == user[username]:
        messagebox.showinfo(title="Success", message="Access granted!")

        # Closes the Login window
        root.destroy()
        menu(username)

    # If the user doesn't enter any information in the textboxes
    # display error message.
    elif username == "" or passwd == "":
        messagebox.showerror("Error", "Please enter a username and/or password!")

    # else display error message
    else:
        if (
            username in user
            and passwd != user[username]
            or username not in user
            and passwd == user[username]
        ):
            messagebox.showerror(
                title="Error",
                message="Access denied! Username or password is incorrect. Please try again.",
            )


# ----Menu Section----


def menu(username):

    menu_win = tk.Tk()
    menu_win.title("Task Manager")
    # menu_win.geometry("500x400")
    menu_win.configure(bg="#333333")
    frame = tk.Frame(bg="#333333")

    title_lbl = tk.Label(
        frame,
        text=f"Welcome, {username}",
        bg="#333333",
        fg="#46a094",
        font=("Arial", 24),
    )

    menu_lbl = tk.Label(
        frame,
        text="Select one of the following options:",
        bg="#333333",
        fg="#ffffff",
        font=("Arial", 15),
    )

    # Options for "admin" and other users
    if username == "admin":

        reg_btn = tk.Button(
            frame,
            text="Register user",
            bg="#333333",
            fg="#ffffff",
            width=15,
            font=("Arial", 10),
            command=lambda: register(),
        )

        add_btn = tk.Button(
            frame,
            text="Add task",
            bg="#333333",
            fg="#ffffff",
            width=15,
            font=("Arial", 10),
            command=lambda: add_task(),
        )

        va_btn = tk.Button(
            frame,
            text="View all tasks",
            bg="#333333",
            fg="#ffffff",
            width=15,
            font=("Arial", 10),
            command=lambda: view_tasks(username, va_btn.cget("text")),
        )

        vm_btn = tk.Button(
            frame,
            text="View my tasks",
            bg="#333333",
            fg="#ffffff",
            width=15,
            font=("Arial", 10),
            command=lambda: view_tasks(username, vm_btn.cget("text")),
        )

        stats_btn = tk.Button(
            frame,
            text="Statistics",
            bg="#333333",
            fg="#ffffff",
            width=15,
            font=("Arial", 10),
            command=lambda: stats(),
        )

        close_btn = tk.Button(
            frame,
            text="Close",
            bg="#333333",
            fg="#ffffff",
            width=15,
            font=("Arial", 10),
            command=menu_win.destroy,
        )

        # Grids
        title_lbl.grid(row=0, column=0, columnspan=2, pady=25, sticky="news")
        menu_lbl.grid(row=1, column=0, pady=5)

        reg_btn.grid(row=2, column=0, pady=5, padx=10, sticky="EW")
        add_btn.grid(row=3, column=0, pady=5, padx=10, sticky="EW")
        va_btn.grid(row=4, column=0, pady=5, padx=10, sticky="EW")
        vm_btn.grid(row=5, column=0, pady=5, padx=10, sticky="EW")
        stats_btn.grid(row=6, column=0, pady=5, padx=10, sticky="EW")

        close_btn.grid(row=7, column=0, pady=20, sticky="ew")

        frame.pack()

        menu_win.mainloop()

    else:

        add_btn = tk.Button(
            frame,
            text="Add task",
            bg="#333333",
            fg="#ffffff",
            width=15,
            font=("Arial", 10),
            command=lambda: add_task(),
        )

        va_btn = tk.Button(
            frame,
            text="View all tasks",
            bg="#333333",
            fg="#ffffff",
            width=15,
            font=("Arial", 10),
            command=lambda: view_tasks(username, va_btn.cget("text")),
        )

        vm_btn = tk.Button(
            frame,
            text="View my tasks",
            bg="#333333",
            fg="#ffffff",
            width=15,
            font=("Arial", 10),
            command=lambda: view_tasks(username, vm_btn.cget("text")),
        )

        close_btn = tk.Button(
            frame,
            text="Close",
            bg="#333333",
            fg="#ffffff",
            width=15,
            font=("Arial", 10),
            command=menu_win.destroy,
        )

        # Grids
        title_lbl.grid(row=0, column=0, columnspan=2, pady=25, sticky="news")
        menu_lbl.grid(row=1, column=0, pady=5)

        add_btn.grid(row=3, column=0, pady=5, padx=10, sticky="EW")
        va_btn.grid(row=4, column=0, pady=5, padx=10, sticky="EW")
        vm_btn.grid(row=5, column=0, pady=5, padx=10, sticky="EW")

        close_btn.grid(row=7, column=0, pady=20, sticky="ew")

        frame.pack()

        menu_win.mainloop()


# ----Register Function----


def register():

    # Creates a child window
    reg_win = tk.Toplevel()
    reg_win.title("Register")
    reg_win.config(bg="#333333")
    frame = tk.Frame(reg_win, bg="#333333")

    reg_label = tk.Label(
        frame,
        text="Please enter the following:",
        bg="#333333",
        fg="#ffffff",
        font=("Arial", 16),
    )

    # Request user to enter a user's username and password
    user_lbl = tk.Label(
        frame, text="Username: ", bg="#333333", fg="#ffffff", font=("Arial", 12)
    )
    passwd_lbl = tk.Label(
        frame, text="Password: ", bg="#333333", fg="#ffffff", font=("Arial", 12)
    )

    new_user = tk.Entry(frame, width=20, font=("Arial", 12))
    new_passwd = tk.Entry(frame, width=20, show="*", font=("Arial", 12))

    # Request the user to re-enter the password
    confirm_lbl = tk.Label(
        frame, text="Confirm password: ", bg="#333333", fg="#ffffff", font=("Arial", 12)
    )
    confirm_new_passwd = tk.Entry(frame, show="*", width=20, font=("Arial", 12))

    # Submits user to user.txt file
    submit_btn = tk.Button(
        frame,
        text="Submit",
        font=("Arial", 12),
        width=10,
        command=lambda: submit_user(
            reg_win,
            new_user.get().lower(),
            new_passwd.get().lower(),
            confirm_new_passwd.get().lower(),
        ),
        bg="#46a094",
        fg="#ffffff",
    )

    # Clears textbox
    clear_btn = tk.Button(
        frame,
        text="Clear",
        font=("Arial", 12),
        width=10,
        command=lambda: clear(reg_win),
        bg="#46a094",
        fg="#ffffff",
    )

    # ----Grids----

    reg_label.grid(row=0, column=0, columnspan=2, padx=5, pady=25, sticky="ew")

    user_lbl.grid(row=1, column=0, pady=5, sticky="w")
    new_user.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    passwd_lbl.grid(row=2, column=0, pady=5, sticky="w")
    new_passwd.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    confirm_lbl.grid(row=3, column=0, pady=5, sticky="w")
    confirm_new_passwd.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    submit_btn.grid(row=4, column=0, padx=5, pady=5, sticky="e")
    clear_btn.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    frame.pack()


# ----Add tasks Function----


# Request the user to assign other users tasks, the name of the task the description and due date.
# Saves the input into tasks.txt file.
def add_task():

    task_win = tk.Toplevel()
    task_win.title("Add Task")
    task_win.config(bg="#333333")
    frame = tk.Frame(task_win, bg="#333333")

    # ----Labels----
    instr_lbl = tk.Label(
        frame,
        text="Please complete the following:",
        bg="#333333",
        fg="#ffffff",
        font=("Arial", 18),
    )

    user_lbl = tk.Label(
        frame,
        text="Select a user: ",
        bg="#333333",
        fg="#ffffff",
        font=("Arial", 12),
    )

    title_lbl = tk.Label(
        frame,
        text="Task title: ",
        bg="#333333",
        fg="#ffffff",
        font=("Arial", 12),
    )

    description_lbl = tk.Label(
        frame,
        text="Task description: ",
        fg="#ffffff",
        bg="#333333",
        font=("Arial", 12),
    )

    due_date_lbl = tk.Label(
        frame,
        text="Select due date: ",
        bg="#333333",
        fg="#ffffff",
        font=("Arial", 12),
    )

    current_date_lbl = tk.Label(
        frame,
        text="Current date: ",
        bg="#333333",
        fg="#ffffff",
        font=("Arial", 12),
    )

    current_date_lbl2 = tk.Label(
        frame,
        text=f"{today.strftime("%d %b %Y")}",
        bg="#333333",
        fg="#ffffff",
        font=("Arial", 12),
    )

    status_lbl = tk.Label(
        frame,
        text="Task complete: ",
        bg="#333333",
        fg="#ffffff",
        font=("Arial", 12),
    )

    task_complete_lbl = tk.Label(
        frame,
        text="No",
        bg="#333333",
        fg="#ffffff",
        font=("Arial", 12),
    )

    # ----Combobox----
    select_user = tk.StringVar()

    user_cmbo = ttk.Combobox(
        frame,
        width=25,
        textvariable=select_user,
        font=("Arial", 12),
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
        command=lambda: submit_tasks(
            select_user.get(),
            task_title_txt.get(),
            task_description_txt.get("1.0", "end-1c"),
            current_date_lbl2.cget("text"),
            task_due_date.selection_get().strftime("%d %b %Y"),
            task_complete_lbl.cget("text"),
            task_win,
        ),
        bg="#46a094",
        fg="#ffffff",
    )

    clear_btn = tk.Button(
        frame,
        text="Clear",
        width=15,
        font=("Arial", 12),
        command=lambda: clear(task_win),
        bg="#46a094",
        fg="#ffffff",
    )

    close_btn = tk.Button(
        frame,
        text="Close",
        width=15,
        font=("Arial", 12),
        command=task_win.destroy,
        bg="#46a094",
        fg="#ffffff",
    )

    # ----Grid layout---

    # ++Labels++
    instr_lbl.grid(
        row=0,
        column=0,
        columnspan=3,
        padx=10,
        pady=25,
        sticky="we",
    )

    user_lbl.grid(
        row=1,
        column=0,
        padx=5,
        pady=5,
        sticky="w",
    )

    title_lbl.grid(
        row=2,
        column=0,
        padx=5,
        pady=5,
        sticky="w",
    )

    description_lbl.grid(
        row=3,
        column=0,
        padx=5,
        pady=5,
        sticky="w",
    )

    due_date_lbl.grid(
        row=4,
        column=0,
        padx=5,
        pady=5,
        sticky="w",
    )

    current_date_lbl.grid(
        row=5,
        column=0,
        padx=5,
        pady=5,
        sticky="w",
    )

    current_date_lbl2.grid(
        row=5,
        column=1,
        padx=5,
        pady=5,
        sticky="w",
    )

    status_lbl.grid(
        row=6,
        column=0,
        padx=5,
        pady=5,
        sticky="w",
    )
    task_complete_lbl.grid(
        row=6,
        column=1,
        padx=5,
        pady=5,
        sticky="w",
    )

    # ++Text and Entry++
    task_title_txt.grid(
        row=2,
        column=1,
        padx=5,
        pady=5,
        sticky="w",
    )

    task_description_txt.grid(
        row=3,
        column=1,
        padx=5,
        pady=5,
        sticky="w",
    )

    # ++Calendar++
    task_due_date.grid(
        row=4,
        column=1,
        padx=5,
        pady=5,
        sticky="w",
    )

    # ++Combobox++
    user_cmbo.grid(
        row=1,
        column=1,
        pady=5,
        padx=5,
        sticky="w",
    )

    # ++buttons++
    save_task_btn.grid(
        row=7,
        column=0,
        padx=5,
        pady=5,
        sticky="e",
    )

    clear_btn.grid(
        row=7,
        column=1,
        padx=5,
        pady=5,
    )

    close_btn.grid(row=7, column=2, padx=5, pady=5, sticky="w")

    frame.pack()


# ----View tasks Section----


def view_tasks(username, menu):
    view_tasks_win = tk.Toplevel()
    view_tasks_win.config(bg="#333333")
    view_tasks_win.resizable(True, True)
    frame = tk.Frame(view_tasks_win, bg="#333333")

    txt_bx = tk.Text(frame, width=48, height=25, wrap="word", font=("Arial", 11))
    # txt_bx.config(state=tk.DISABLED)  # Prevents users from editing the text box.

    vert_scroll = ttk.Scrollbar(frame, orient="vertical", command=txt_bx.yview)
    horizon_scroll = ttk.Scrollbar(frame, orient="horizontal", command=txt_bx.xview)

    close_btn = tk.Button(
        frame,
        text="Close",
        width=15,
        font=("Arial", 12),
        command=view_tasks_win.destroy,
        bg="#46a094",
        fg="#ffffff",
    )

    if menu == "View all tasks":

        view_tasks_win.title("View All Tasks")

        # ---- Widgets ----
        info_lbl = tk.Label(
            frame,
            text="List of all the tasks",
            bg="#333333",
            fg="#ffffff",
            font=("Arial", 20),
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

                        display_tasks(
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

        close_btn.grid(row=10, column=1, columnspan=4, pady=10, sticky="ew")

        # ---- Scrollbar ----
        txt_bx["yscrollcommand"] = vert_scroll.set
        txt_bx["xscrollcommand"] = horizon_scroll.set

    elif menu == "View my tasks":

        view_tasks_win.title("My Tasks")
        current_user.clear()
        task_num_list.clear()

        try:

            read_my_tasks(username, txt_bx)

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
            command=lambda: update_task(
                txt_bx,
                username,
                chg_task_num_cmbo,
                chg_title,
                chg_user_cmbo,
                chg_descript,
                chg_status,
                chg_due_date_cal,
            ),
        )

        # ---- Bindings ----
        chg_task_num_cmbo.bind(
            "<<ComboboxSelected>>",
            lambda event: search_list_event(
                event,
                frame,
                chg_task_num_cmbo,
                chg_title,
                chg_user_cmbo,
                chg_descript,
                chg_status,
                chg_due_date_cal,
                txt_bx,
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

        close_btn.grid(row=9, column=3, pady=10, sticky="ew")
        update_btn.grid(row=9, column=2, pady=10, sticky="ew")

    frame.pack()


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


# =============Other Functions=============

# ----Clear text----


def clear(root):

    for widget in root.winfo_children():
        # Clears all Entry Widgets
        if isinstance(widget, tk.Entry):
            widget.delete(0, tk.END)
        elif not isinstance(widget, tk.Entry):
            clear(widget)

        # Clears all Text Widgets
        """if isinstance(widget, tk.Text):
            widget.delete("1.0", tk.END)
        elif not isinstance(widget, tk.Text):
            clear(widget)"""


# ----Submit Tasks----


def submit_tasks(
    user_task,
    task_title,
    task_description,
    current_date,
    task_due_date,
    task_complete,
    root,
):

    try:

        # Append user input and format the output to task.txt
        with open("tasks.txt", "a", encoding="utf-8") as file:

            # Write to task.txt file
            file.writelines(
                f"\n{user_task}, {task_title}, {task_description}, {current_date}, {task_due_date}, {task_complete}"
            )
        messagebox.showinfo(title="Success", message="New task saved!")
        root.destroy()

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="File not found!")


# ----Submit User----


def submit_user(root, new_user, new_passwd, confirm_new_passwd):
    try:
        with open("user.txt", "a") as add_line:

            if new_user in user:
                messagebox.showwarning(
                    "Warning",
                    f"The username '{new_user}', already exists! Please enter a new user name.",
                )
            else:
                if new_passwd == confirm_new_passwd:

                    add_line.writelines(f"\n{new_user}, {confirm_new_passwd}")
                    messagebox.showinfo("Success", "New user successfully saved!")
                    root.destroy()

                # If the user enters nothing for either password or confirm password textbox
                # display warning
                elif (
                    new_passwd == ""
                    or confirm_new_passwd == ""
                    or (new_passwd == "" and confirm_new_passwd == "")
                ):
                    messagebox.showwarning(
                        "Warning",
                        "No, input. Please enter a password for the new user.",
                    )

                # Else request the user to re-enter the passwords until they match
                else:
                    messagebox.showerror(
                        "Error", "The passwords do not match! Please try again!"
                    )

    except Exception as error:
        messagebox.showerror("Error", f"An error has occurred: {error}")


# ----View Tasks---


def display_tasks(
    txt_bx,
    count,
    title,
    assigned_user,
    assigned_date,
    due_date,
    complete_task,
    description,
):
    # ---- Text box ----
    # Print input to the format below
    """
    Example of the format:
    _________________________________________________
    No.:                      1
    Task:                     Assign initial tasks
    Assigned to:              admin
    Date assigned:            10 Oct 2019
    Date due:                 25 oct 2019
    Task complete?            No

    Task description:
        Use task_manager.py to assign each team member with appropriate tasks
    _________________________________________________
    """

    txt_bx.insert(tk.END, "_______________________________________________\n")

    txt_bx.insert(tk.END, f"No.: \t\t{count:>2}\n")
    txt_bx.insert(tk.END, f"Task: \t\t{title :>8}\n")
    txt_bx.insert(tk.END, f"Assigned to: \t\t{assigned_user :>6}\n")
    txt_bx.insert(tk.END, f"Date assigned: \t\t{assigned_date :>3}\n")
    txt_bx.insert(tk.END, f"Date due: \t\t{due_date :>3}\n")
    txt_bx.insert(tk.END, f"Task complete? \t\t{complete_task}\n")
    txt_bx.insert(tk.END, f"Task description:\n {description}\n")

    txt_bx.insert(tk.END, "_______________________________________________\n")


# ----Check_file Section-----


def check_file():
    task_file = os.path.isfile("tasks.txt")
    user_file = os.path.isfile("user.txt")

    if user_file == True and task_file == True:
        read_users()
    else:
        print(
            "The files for the program does not exist. Download the files from the repo, then run the program again."
        )
        exit()


# ----Read_data Section----


# +++user.txt+++
def read_users():
    try:
        # Open the user.txt file and read the lines
        with open("user.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

            # Traverse through the file'
            for line in lines:
                # Strip the string of the newline character \n
                # Split the string by the comma and the space ","
                split_lines = line.strip().split(", ")
                check_username.append(split_lines[0])
                check_passwd.append(split_lines[1])

        # Create a dictionary to check the user credentials
        for i, j in zip(check_username, check_passwd):
            user.update({i: j})

    except FileNotFoundError as error:
        print(f"An error occurred: {error}")


# +++tasks.txt for current user+++
def read_my_tasks(username, txt_bx):

    # ---- Read File ----

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

                display_tasks(
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


# ----Update data Section----


def update_task(
    txt_bx,
    username,
    chg_tsk_num_cmbo,
    chg_title,
    chg_user_cmbo,
    chg_descript,
    chg_status,
    chg_due_date_cal,
):
    try:
        for task in current_user:

            # Gets the selected task number.
            if task["No"] == chg_tsk_num_cmbo.get():
                tsk_num = int(task["No"])
                tsk_user = chg_user_cmbo.get().strip()
                tsk_title = chg_title.get("1.0", tk.END).strip()
                tsk_descript = chg_descript.get("1.0", tk.END).strip()
                tsk_assign_date = task["assigned date"]
                tsk_status = chg_status.get().strip()
                tsk_due_date = chg_due_date_cal.selection_get().strftime("%d %b %Y")

                # Checks for the correct task number
                with open("tasks.txt", "r", encoding="utf-8") as find_line:
                    line = find_line.readlines()
                    line[tsk_num - 1] = (
                        f"{tsk_user}, {tsk_title}, {tsk_descript}, {tsk_assign_date}, {tsk_due_date}, {tsk_status}\n"
                    )

                # Update that specific task
                with open("tasks.txt", "w", encoding="utf-8") as update_line:
                    update_line.writelines(line)

        current_user.clear()
        txt_bx.delete("1.0", tk.END)

        read_my_tasks(username, txt_bx)

    except Exception as error:
        messagebox.showerror("Error", f"Failed to update task. {error}")

    
# ----Search list Section----


#  +++ Binding Event
def search_list_event(
    event,
    frame,
    chg_task_num_cmbo,
    chg_title,
    chg_user_cmbo,
    chg_descript,
    chg_status,
    chg_due_date_cal,
    txt_bx,
):

    # Clear all entry widgets everytime the button is clicked.
    clear(frame)
    chg_descript.delete("1.0", tk.END)
    chg_title.delete("1.0", tk.END)
    txt_bx.delete("1.0", tk.END)

    # Search through a list of dictionaries.
    for task in current_user:

        display_tasks(
            txt_bx,
            task["No"],
            task["title"],
            task["username"],
            task["assigned date"],
            task["due date"],
            task["complete task"],
            task["description"],
        )

        # If task is incomplete set the values in the correct widget.
        if task["No"] == chg_task_num_cmbo.get():
            chg_task_num_cmbo.set(f"{task['No']}")
            chg_user_cmbo.set(f"{task['username']}")
            chg_title.insert(tk.END, f"{task['title'].lstrip()}")
            chg_descript.insert(tk.END, f"{task['description'].lstrip()}")
            chg_status.insert(tk.END, task["complete task"].lstrip())
            convert_date = datetime.strptime(task["due date"].lstrip(), "%d %b %Y")
            chg_due_date_cal.selection_set(convert_date)


#   +++ Button Event (No longer in use) +++
def search_list(
    frame,
    chg_task_num_cmbo,
    chg_title,
    chg_user_cmbo,
    chg_descript,
    chg_status,
    chg_due_date_cal,
):
    # Clear all entry widgets everytime the button is clicked.
    clear(frame)
    chg_descript.delete("1.0", tk.END)

    # The default value is the current user.
    chg_user_cmbo.set(f"{username}")
    chg_task_num_cmbo.set(chg_task_num_cmbo.get())

    # Search through a list of dictionaries.
    for task in current_user:

        # If task is incomplete set the values in the correct widget.
        if task["No"] == chg_task_num_cmbo.get():
            chg_task_num_cmbo.set(f"{task['No']}")
            chg_user_cmbo.set(f"{task['username']}")
            chg_title.insert(tk.END, f"{task['title']}")
            chg_descript.insert(tk.END, f"{task['description']}")
            chg_status.insert(tk.END, task["complete task"])
            convert_date = datetime.strptime(task["due date"].lstrip(), "%d %b %Y")
            chg_due_date_cal.selection_set(convert_date)


# ===============Main Function===============

if __name__ == "__main__":
    check_file()

    # =====GUI Configuration=====
    root = tk.Tk()
    root.title("Login")
    root.geometry("440x320")  # width x height
    root.configure(bg="#333333")
    frame = tk.Frame(bg="#333333")

    # ====Login Window====
    # Request the user to enter the username
    login_lbl = tk.Label(
        frame,
        text="Login",
        bg="#333333",
        fg="#46a094",
        font=("Arial", 30),
    )
    user_lbl = tk.Label(
        frame,
        text="Username:",
        bg="#333333",
        fg="#ffffff",
        font=("Arial", 14),
    )
    passwd_lbl = tk.Label(
        frame,
        text="Password:",
        bg="#333333",
        fg="#ffffff",
        font=("Arial", 14),
    )

    username = tk.Entry(frame, font=("Arial", 14))
    passwd_entry = tk.Entry(frame, show="*", font=("Arial", 14))

    # executes the login method when clicked
    login_btn = tk.Button(
        frame,
        text="Login",
        width=8,
        command=lambda: login(username.get().lower(), passwd_entry.get().lower()),
        bg="#46a094",
        fg="#ffffff",
        font=("Arial", 14),
    )

    # Clears entry boxes
    clear_btn = tk.Button(
        frame,
        text="Clear",
        width=8,
        command=lambda: clear(root),
        bg="#46a094",
        fg="#ffffff",
        font=("Arial", 14),
    )

    # ----Grids----
    login_lbl.grid(row=0, column=0, columnspan=3, pady=25, sticky="news")

    user_lbl.grid(row=1, column=0, pady=5, sticky="w")
    username.grid(row=1, column=1, columnspan=2, padx=5, pady=10, sticky="w")

    passwd_lbl.grid(row=2, column=0, pady=5, sticky="w")
    passwd_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=10, sticky="w")

    login_btn.grid(row=3, column=1, pady=10, sticky="ew")
    clear_btn.grid(row=3, column=2, pady=10, sticky="ew")

    # .pack() is responsive, looks better than grid
    frame.pack()
    root.mainloop()

# ====References====
"""
    Added items to empty user dictionary. Check login section
    - https://www.geeksforgeeks.org/adding-items-to-a-dictionary-in-a-loop-in-python/

    Updating dictionary, see register user method
    - https://www.w3schools.com/python/python_dictionaries_add.asp

    Creating the simple GUI
    - https://www.makeuseof.com/python-login-page-simple-build/
    - https://www.youtube.com/watch?v=MeMCBdnhvQs
    - https://www.w3resource.com/python-exercises/tkinter/python-tkinter-layout-management-exercise-3.php

    Colour palette
    - https://za.pinterest.com/pin/330310953935935490/

    Clearing the widgets:
    - https://www.youtube.com/watch?v=IFcIVl6da5o

    Closing a window, without a button:
    - https://stackoverflow.com/questions/67295637/closing-current-window-when-opening-a-new-window-in-tkinter-python

    Changing the size of buttons:
    - https://www.tutorialspoint.com/how-do-i-change-button-size-in-python-tkinter

    Fixed the closing error for the main menu
    - https://stackoverflow.com/questions/21645716/cannot-invoke-button-command-application-has-been-destroyed

    Fixed an error caused by frame and pack
    - https://stackoverflow.com/questions/23584325/cannot-use-geometry-manager-pack-inside

    Solves the frame issue for TopLevel Widgets
    - https://stackoverflow.com/questions/52950267/tkinter-frame-in-toplevel-displayed-in-parent

    Solves the issue of clearing all entry window
    - https://stackoverflow.com/questions/69866188/python-is-there-a-way-to-clear-all-entry-boxes-in-a-tkinter-ui-in-one-line

    Calendar: installation and creation of gui
    - https://dev.to/zettasoft/how-to-make-a-calendar-using-python-tkinter-4ijj
    - https://www.geeksforgeeks.org/create-a-date-picker-calendar-tkinter/

    Alignment of widgets
    - https://stackoverflow.com/questions/74418639/aligning-entries-buttons-with-tkinter

    Get the text of the button:
    - https://stackoverflow.com/questions/26765218/get-the-text-of-a-button-widget

    Fixed line 465 - TypeError: descriptor 'strftime' for 'datetime.date' objects doesn't apply to a 'str' object:
    - https://stackoverflow.com/questions/30112357/typeerror-descriptor-strftime-requires-a-datetime-date-object-but-received

    Functions of tkCalendar:
    - https://tkcalendar.readthedocs.io/en/stable/Calendar.html

    Fixed date conversion error for search_list:
    - https://stackoverflow.com/questions/25015711/time-data-does-not-match-format

    Removed the search button and adding bindings to chg_task_num_cmbo:
    - https://stackoverflow.com/questions/73238441/tkinter-how-to-pass-arguments-when-comboboxselected-is-bound-to-a-method
"""
