# ====Import Libraries====
from datetime import date
from tkinter import messagebox
from tkcalendar import *
from menu_functions.main_menu_gui import menu
from menu_functions.functions import check_file, clear
import tkinter as tk

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
        menu(username, check_username, current_user, task_num_list, today)

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


# ===============Main Function===============

if __name__ == "__main__":
    check_file(check_username, check_passwd, user)

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

    Fixed the issue with import functions from the same folder:
    - https://stackoverflow.com/questions/43865291/import-function-from-a-file-in-the-same-folder
"""
