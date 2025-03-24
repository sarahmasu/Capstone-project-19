# ====Import Libraries====
from datetime import date
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *

# ====Dictionaries & Lists====
# Store the usernames and passwords to be retrieved later on in the code
check_username = []
check_passwd = []
user = {}

# ====Read_data Section====


def read_data():
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


# ====Login Section====


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


# ====Menu Section====


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
        font=("Arial", 12),
    )

    # Options
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
        )

        vm_btn = tk.Button(
            frame,
            text="View my tasks",
            bg="#333333",
            fg="#ffffff",
            width=15,
            font=("Arial", 11),
        )

        stats_btn = tk.Button(
            frame,
            text="Statistics",
            bg="#333333",
            fg="#ffffff",
            width=15,
            font=("Arial", 11),
        )

        close_btn = tk.Button(
            frame,
            text="Close",
            bg="#333333",
            fg="#ffffff",
            width=15,
            font=("Arial", 11),
            command=menu_win.destroy,
        )

        # Grids
        title_lbl.grid(row=0, column=0, columnspan=2, pady=25, sticky="news")
        menu_lbl.grid(row=1, column=0, pady=5)

        reg_btn.grid(row=2, column=0, pady=5, padx=10, sticky="w")
        add_btn.grid(row=3, column=0, pady=5, padx=10, sticky="W")
        va_btn.grid(row=4, column=0, pady=5, padx=10, sticky="W")
        vm_btn.grid(row=5, column=0, pady=5, padx=10, sticky="W")
        stats_btn.grid(row=6, column=0, pady=5, padx=10, sticky="W")

        close_btn.grid(row=7, column=0, pady=20, sticky="news")

        frame.pack()

        menu_win.mainloop()


# ====Register Function====


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
        font=("Arial", 12),
    )

    # Request user to enter a user's username and password
    user_lbl = tk.Label(
        frame, text="Username: ", bg="#333333", fg="#ffffff", font=("Arial", 12)
    )
    passwd_lbl = tk.Label(
        frame, text="Password: ", bg="#333333", fg="#ffffff", font=("Arial", 12)
    )

    new_user = tk.Entry(frame, font=("Arial", 12))
    new_passwd = tk.Entry(frame, show="*", font=("Arial", 12))

    # Request the user to re-enter the password
    confirm_lbl = tk.Label(
        frame, text="Confirm password: ", bg="#333333", fg="#ffffff", font=("Arial", 12)
    )
    confirm_new_passwd = tk.Entry(frame, show="*", font=("Arial", 12))

    # Submits user to user.txt file
    submit_btn = tk.Button(
        frame,
        text="Submit",
        font=("Arial", 12),
        command=lambda: submit_user(
            new_user.get().lower(),
            new_passwd.get().lower(),
            confirm_new_passwd.get().lower(),
        ),
    )

    # Clears textbox
    clear_btn = tk.Button(
        frame,
        text="Clear",
        font=("Arial", 12),
        command=lambda: clear(reg_win),
    )

    # Method check whether the passwords match
    # If the passwords match append the new user and their password to the user.txt file

    # ===Submit User===
    def submit_user(new_user, new_passwd, confirm_new_passwd):
        with open("user.txt", "a") as add_line:

            if new_passwd == confirm_new_passwd:

                add_line.writelines(f"\n{new_user}, {confirm_new_passwd}")
                messagebox.showinfo("Success", "New user successfully saved!")
                reg_win.destroy()

            # If the user enters nothing for either password or confirm password textbox
            # display warning
            elif (
                new_passwd == ""
                or confirm_new_passwd == ""
                or (new_passwd == "" and confirm_new_passwd == "")
            ):
                messagebox.showwarning(
                    "No Input", "Please enter a password for the new user."
                )

            # Else request the user to re-enter the passwords until they match
            else:
                messagebox.showerror(
                    "Error", "The passwords do not match! Please try again!"
                )

    # Grids
    frame.grid(row=0, column=0)
    reg_label.grid(columnspan=2, pady=25)

    user_lbl.grid(row=1, column=0, pady=5)
    new_user.grid(row=1, column=1, padx=5, pady=10)

    passwd_lbl.grid(row=2, column=0, pady=5)
    new_passwd.grid(row=2, column=1, padx=5, pady=10)

    confirm_lbl.grid(row=3, column=0, pady=5)
    confirm_new_passwd.grid(row=3, column=1, padx=5, pady=10)

    submit_btn.grid(row=4, column=0, padx=15, pady=15)
    clear_btn.grid(row=4, column=1, pady=15)


# ====Add tasks Function====


# Request the user to assign other users tasks, the name of the task the description and due date.
# Saves the input into tasks.txt file.
def add_task():

    task_win = tk.Toplevel()
    task_win.title("Add Task")
    task_win.config(bg="#333333")
    frame = tk.Frame(task_win, bg="#333333")

    # Get current date and format it to dd/MMM/YYYY
    today = date.today()

    # ----Labels----
    instr_lbl = tk.Label(
        frame,
        text="Please complete the following:",
        bg="#333333",
        fg="#ffffff",
        font=("Arial", 14),
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
        text="Due date (dd Mon YYYY): ",
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

    current_date = tk.Label(
        frame,
        text=f"{today.strftime("%d %b %Y")}",
        bg="#333333",
        fg="#ffffff",
        font=("Arial", 12),
    )

    status_lbl = tk.Label(
        frame,
        text="Completion status: ",
        bg="#333333",
        fg="#ffffff",
        font=("Arial", 12),
    )

    task_complete = tk.Label(
        frame,
        text="Incomplete",
        bg="#333333",
        fg="#ffffff",
        font=("Arial", 12),
    )

    # ----Combobox----
    select_user = tk.StringVar()

    user_cmbo = ttk.Combobox(
        frame, width=18, textvariable=select_user, font=("Arial", 12)
    )

    user_cmbo["values"] = tuple(check_username)

    user_cmbo["state"] = "readonly"

    user_task = select_user.get()

    # ----Entry boxes----
    task_title = tk.Entry(frame, width=20, font=("Arial", 12))

    task_description = tk.Entry(frame, width=20, font=("Arial", 12))

    task_due_date = tk.Entry(frame, width=20, font=("Arial", 12))

    # ----Buttons----
    save_task_btn = tk.Button(
        frame,
        text="Submit",
        width= 10,
        font=("Arial", 12),
        command=lambda: submit_tasks(
            user_task,
            task_title.get(),
            task_description.get(),
            current_date.get(),
            task_due_date.get(),
            task_complete.get(),
        ),
    )

    clear_btn = tk.Button(
        frame,
        text="Clear",
        width=10,
        font=("Arial", 12),
        command=lambda: clear(task_win),
    )

    close_btn = tk.Button(
        frame,
        text="Close",
        width=15,
        font=("Arial", 12),
        command=task_win.destroy,
    )

    # ----Grid layout---

    frame.grid(row=0, column=0)
    instr_lbl.grid(row=0, column=0, columnspan=2, pady=25, sticky= "we",)

    user_lbl.grid(row=1, column=0, padx = 5, pady=5, sticky= "w",)
    user_cmbo.grid(row=1, column=1, pady=5, padx=5, sticky="w",)

    title_lbl.grid(row=2, column=0, padx = 5, pady=5, sticky= "w",)
    task_title.grid(row=2, column=1, padx=5, pady=5, sticky="w",)

    description_lbl.grid(row=3, column=0, padx = 5, pady=5, sticky= "w",)
    task_description.grid(row=3, column=1, padx=5, pady=5, sticky="w",)

    due_date_lbl.grid(row=4, column=0, padx = 5, pady=5, sticky= "w",)
    task_due_date.grid(row=4, column=1, padx=5, pady=5, sticky="w",)

    current_date_lbl.grid(row=5, column=0, padx = 5, pady=5, sticky= "w",)
    current_date.grid(row=5, column=1, padx=5, pady=5, sticky="w",)

    status_lbl.grid(row=6, column=0, padx = 5, pady=5, sticky= "w",)
    task_complete.grid(row=6, column=1, padx=5, pady=5, sticky="w",)

    save_task_btn.grid(row=7, column=0, padx=15, pady=5, sticky="we",)
    clear_btn.grid(row=7, column=1, padx=15, pady=5, sticky="we",)
    close_btn.grid(row=7, column=2, padx=15, pady=5, sticky="we",)

    # ----Methods----

    def submit_tasks(
        user_task,
        task_title,
        task_description,
        current_date,
        task_due_date,
        task_complete,
    ):

        # Append user input and format the output to task.txt
        with open("tasks.txt", "a", encoding="utf-8") as file:

            # Write to task.txt file
            file.writelines(
                f"\n{user_task}, {task_title}, {task_description}, {current_date}, {task_due_date}, {task_complete}"
            )
        messagebox.showinfo(title="Success", text="Successfully saved task.")

    task_win.mainloop()

# ====Display output Section====


def display_output(
    title, assigned_user, assigned_date, due_date, complete_task, description
):
    # Print the output similar to output 2
    print("_________________________________________________\n")

    print(f"Task: \t\t\t{ title :>10}")
    print(f"Assigned to: \t\t{assigned_user :>6}")
    print(f"Date assigned: \t\t{assigned_date :>3}")
    print(f"Date due: \t\t{due_date :>3}")
    print(f"Task complete? \t\t{complete_task}")
    print(f"Task description:\n {description}")

    print("_________________________________________________\n")


# ====View tasks Section====


def view_tasks(menu):
    if menu == "va":
        # Read the task.txt file to display all the task and which user is assign to it
        with open("tasks.txt", "r", encoding="utf-8") as read_all_tasks:
            lines = read_all_tasks.readlines()

            # Iterate through task.txt file
            for line in lines:
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

                display_output(
                    title,
                    assigned_user,
                    assigned_date,
                    due_date,
                    complete_task,
                    description,
                )

    elif menu == "vm":
        # Read the task.txt file
        with open("tasks.txt", "r", encoding="utf-8") as read_my_tasks:
            lines = read_my_tasks.readlines()

            # Iterate through task.txt file
            for line in lines:
                # Split the lines where there is a comma and a space
                split_lines = line.split(",")

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

                    # Print the output similar to output 2
                    display_output(
                        my_title,
                        my_username,
                        my_assigned_date,
                        my_due_date,
                        my_complete_task,
                        my_description,
                    )

    else:
        print("Incorrect option.")


# ====Clear text====


def clear(root):

    # Clears all entry boxes
    for widget in root.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.delete(0, "end")
        elif not isinstance(widget, tk.Entry):
            clear(widget)


# ===============Main Function===============

if __name__ == "__main__":
    read_data()

    # =====GUI Configuration=====
    root = tk.Tk()
    root.title("Login")
    root.geometry("440x340")  # width x height
    root.configure(bg="#333333")
    frame = tk.Frame(bg="#333333")

    # ====Login Window====
    # Request the user to enter the username
    login_lbl = tk.Label(
        frame, text="Login", bg="#333333", fg="#46a094", font=("Arial", 30)
    )
    user_lbl = tk.Label(
        frame, text="Username:", bg="#333333", fg="#ffffff", font=("Arial", 14)
    )
    passwd_lbl = tk.Label(
        frame, text="Password:", bg="#333333", fg="#ffffff", font=("Arial", 14)
    )

    username = tk.Entry(frame, font=("Arial", 14))
    passwd_entry = tk.Entry(frame, show="*", font=("Arial", 14))

    # executes the login method when clicked
    login_btn = tk.Button(
        frame,
        text="Login",
        width = 10,
        command=lambda: login(username.get().lower(), passwd_entry.get().lower()),
        bg="#46a094",
        fg="#ffffff",
        font=("Arial", 14),
    )

    # Clears entry boxes
    clear_btn = tk.Button(
        frame,
        text="Clear",
        width = 5,
        command=lambda: clear(root),
        bg="#46a094",
        fg="#ffffff",
        font=("Arial", 14),
    )

    # Grids
    login_lbl.grid(row=0, column=0, columnspan=2, pady=25, sticky="news")

    user_lbl.grid(row=1, column=0, pady=5, sticky="w")
    username.grid(row=1, column=1, columnspan=2, padx=5, pady=10, sticky="w")

    passwd_lbl.grid(row=2, column=0, pady=5, sticky="w")
    passwd_entry.grid(row=2, column=1,columnspan=2, padx=5, pady=10, sticky="w")

    login_btn.grid(row=3, column=0, padx=5, pady=15,)
    clear_btn.grid(row=3, column=1, padx=5, pady=15,)

    # .pack() is responsive, looks better than grid
    frame.pack()
    root.mainloop()

    # ====Menu Window====
    '''print(f"Welcome, {username.get().lower()}")

    while True:
        # Present the menu to the user and
        # make sure that the user input is converted to lower case.
        if username == "admin":
            menu = input(
                """Select one of the following options:
        r - register a user
        a - add task
        va - view all tasks
        vm - view my tasks
        s - statistics
        e - exit
        : """
            ).lower()

            if menu == "r":
                # Allows only user "admin" to add new users
                if username == "admin":
                    register()
                else:
                    print("Only admins are allowed to register new users.")

            elif menu == "a":
                add_task()

            elif menu == "va":
                view_tasks(menu)

            elif menu == "vm":
                view_tasks(menu)

            elif menu == "s":
                # Reads the task.txt
                # Counts the number of tasks
                # prints the total number of tasks in the file
                # Reads the user.txt file, counts the number of users
                # prints end results
                with open("tasks.txt", "r") as read:
                    total_tasks = len(read.readlines())
                    print(f"Total number of tasks: {total_tasks}")

                with open("user.txt", "r") as read:
                    total_user = len(read.readlines())
                    print(f"Total number of users: {total_user}")

            elif menu == "e":
                print("Goodbye!!!")
                exit()

            else:
                print("You have made entered an invalid input. Please try again")

        else:
            menu = input(
                """Select one of the following options:
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
    : """
            ).lower()

        if menu == "a":
            add_task()

        elif menu == "va":
            view_tasks(menu)

        elif menu == "vm":
            view_tasks(menu)

        elif menu == "e":
            print("Goodbye!!!")
            exit()

        else:
            print("You have made entered an invalid input. Please try again")'''

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
"""
