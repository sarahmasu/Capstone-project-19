# =============Libraries=============
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from tkcalendar import *
import os.path

# =============Function=============

# ----Read_data Section----


# +++user.txt+++
def read_users(check_username, check_passwd, user):
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
# don't use this function
def read_my_tasks(username, txt_bx, current_user):

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


def submit_user(root, user, new_user, new_passwd, confirm_new_passwd):
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

    txt_bx.insert(tk.END, f"_______________________________________________\n")

    txt_bx.insert(tk.END, f"No.: \t\t{count:>2}\n")
    txt_bx.insert(tk.END, f"Task: \t\t{title :>8}\n")
    txt_bx.insert(tk.END, f"Assigned to: \t\t{assigned_user :>6}\n")
    txt_bx.insert(tk.END, f"Date assigned: \t\t{assigned_date :>3}\n")
    txt_bx.insert(tk.END, f"Date due: \t\t{due_date :>3}\n")
    txt_bx.insert(tk.END, f"Task complete? \t\t{complete_task}\n")
    txt_bx.insert(tk.END, f"Task description:\n {description}\n")

    txt_bx.insert(tk.END, f"_______________________________________________\n")


# ----Check_file Section-----


def check_file(check_username, check_passwd, user):
    task_file = os.path.isfile("tasks.txt")
    user_file = os.path.isfile("user.txt")

    if user_file == True and task_file == True:
        read_users(check_username, check_passwd, user)
    else:
        print(
            "The files for the program does not exist. Download the files from the repo, then run the program again."
        )
        exit()


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
    current_user,
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

        read_my_tasks(username, txt_bx, current_user)

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
    current_user,
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
    username,
    current_user,
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

# ----Generate report----
    # ____Explanation___
    """
        Function generates reports and creates two text files, 
        task_overview.txt and user_overview.txt, based on the
        information from user.txt and tasks.txt files. The files and be
        viewed by admin.

        task_overview.txt file contains:
            - Counts the total number of tasks.
            - Counts the total number of complete and incomplete tasks.
            - Counts the total number of incomplete and overdue tasks.
            - Calculates the percentage of complete and incomplete tasks.
            - Calculates the percentage of incomplete and incomplete tasks.

        user_overview.txt file contains:
            - Counts the total number of users.
            - Counts the total number of users assigned tasks.
            - Calculate the percentage of incomplete assigned tasks.
            - Calculate the percentage of complete and overdue tasks.
            - Calculate the percentage of complete assigned tasks.
    """


def generate_report(check_username):

    total_overdue_incomplete = 0
    total_incomplete_task = 0
    total_complete_task = 0

    count_complete_users = 0
    count_incomplete_users = 0
    count_overdue_user = 0
