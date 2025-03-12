# ====Import Libraries====
from datetime import date
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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

    # Closes the Login window
    root.destroy()

    menu_win = tk.Tk()
    menu_win.title("Task Manager")
    menu_win.geometry("500x400")
    menu_win.configure(bg="#333333")
    frame = tk.Frame(bg="#333333")

    if username == "admin":
        title_lbl = tk.Label(
            frame,
            text=f"Welcome, {username}",
            bg="#333333",
            fg="#46a094",
            font=("Arial", 30),
        )

        menu_lbl = tk.Label(
            frame,
            text="Select one of the following options:",
            bg="#333333",
            fg="#ffffff",
            font=("Arial", 14),
        )

        var = tk.IntVar()

        reg_btn = tk.Button(
            frame,
            text="Register a user",
            variable=var,
            value=0,
            bg="#333333",
            fg="#ffffff",
            font=("Arial", 12),
        )

        add_btn = tk.Button(
            frame,
            text="Add task",
            variable=var,
            value=0,
            bg="#333333",
            fg="#ffffff",
            font=("Arial", 12),
        )

        va_btn = tk.Button(
            frame,
            text="View all tasks",
            variable=var,
            value=0,
            bg="#333333",
            fg="#ffffff",
            font=("Arial", 12),
        )

        vm_btn = tk.Button(
            frame,
            text="View my tasks",
            variable=var,
            value=0,
            bg="#333333",
            fg="#ffffff",
            font=("Arial", 12),
        )

        stats_btn = tk.Button(
            frame,
            text="Statistics",
            variable=var,
            value=0,
            bg="#333333",
            fg="#ffffff",
            font=("Arial", 12),
        )

        # Grids
        title_lbl.grid(row=0, column=0, columnspan=2, pady=25, sticky="news")
        menu_lbl.grid(row=1, column=0, pady=5)

        reg_btn.grid(row=2, column=0,pady=5, sticky="W")
        add_btn.grid(row=3, column=0,pady=5, sticky="W")
        va_btn.grid(row=4, column=0,pady=5, sticky="W")
        vm_btn.grid(row=5, column=0,pady=5, sticky="W")
        stats_btn.grid(row=6, column=0,pady=5, sticky="W")

        frame.pack()
        # Remove in case an error arises
        root.mainloop()

# ====Register Section====


def register():

    # Request user to enter a user's username and password
    new_user = input("\nEnter new user's username: ").lower()
    new_passwd = input("Enter new user's password: ").lower()

    # Request the user to re-enter the password
    confirm_new_passwd = input("Confirm password: ").lower()

    # Check whether the passwords match
    # If the passwords match append the new user and their password to the user.txt file
    with open("user.txt", "a", encoding="utf-8") as add_file:
        if new_passwd == confirm_new_passwd:
            add_file.writelines(f"\n{new_user}, {confirm_new_passwd}")
            print("New user and password saved!")

        # Else request the user to re-enter the passwords until they match
        else:
            while new_passwd != confirm_new_passwd:
                print("\nThe passwords do not match, please try again.")
                new_passwd = input("Enter new user's password: ").lower()
                confirm_new_passwd = input("Confirm password: ").lower()

                if new_passwd == confirm_new_passwd:
                    add_file.writelines(f"\n{new_user}, {confirm_new_passwd}")
                    print("New user and password saved!")
                    break

                elif new_passwd == "":
                    print(f"\nPlease enter a password for the new user.")
                    new_passwd = input("Enter new user's password: ").lower()
                    confirm_new_passwd = input("Confirm password: ").lower()

    # user.update({new_user: new_passwd})


# ====Add tasks Section====


def add_task():
    # Append user input and format the output to task.txt
    with open("tasks.txt", "a", encoding="utf-8") as file:
        # Request the user to assign other users tasks, the name of the task,
        # the description and when it's due
        user_task = input("\nEnter the user you want to assign a task to: ")
        task_title = input("Enter the title of the task: ")
        task_description = input("Enter the description of the task: ")
        task_due_date = input("Enter the due date of the task (dd Mon YYYY): ")

        # Get current date and format it to dd/MMM/YYYY
        today = date.today()
        current_date = today.strftime("%d %b %Y")

        # The default value of task_complete
        task_complete = "No"

        # Write to task.txt file
        file.writelines(
            f"\n{user_task}, {task_title}, {task_description}, {current_date}, {task_due_date}, {task_complete}"
        )


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


def clear():

    # Clears all entry boxes
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.delete(0, "end")


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
        command=lambda: login(username.get().lower(), passwd_entry.get().lower()),
        bg="#46a094",
        fg="#ffffff",
        font=("Arial", 14),
    )

    # Clears entry boxes
    clear_btn = tk.Button(
        frame,
        text="Clear",
        command=lambda: clear(),
        bg="#46a094",
        fg="#ffffff",
        font=("Arial", 14),
    )

    # Grids
    login_lbl.grid(row=0, column=0, columnspan=2, pady=25, sticky="news")

    user_lbl.grid(row=1, column=0, pady=5)
    username.grid(row=1, column=1, padx=5, pady=10)

    passwd_lbl.grid(row=2, column=0, pady=5)
    passwd_entry.grid(row=2, column=1, padx=5, pady=10)

    login_btn.grid(row=3, column=0, columnspan=1, padx=15, pady=15)
    clear_btn.grid(row=3, column=1, columnspan=2, padx=15, pady=15)

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
"""
