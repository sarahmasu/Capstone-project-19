# ====Import Libraries====
from tkinter import messagebox
import Scripts.main_menu_gui as main
import Scripts.functions as fun
import tkinter as tk


# =====GUI Configuration=====
def login(user, check_username, current_user, task_num_list, today):
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
        command=lambda: login_user(
            root,
            username.get().lower(),
            passwd_entry.get().lower(),
            user,
            check_username,
            current_user,
            task_num_list,
            today,
        ),
        bg="#46a094",
        fg="#ffffff",
        font=("Arial", 14),
    )

    # Clears entry boxes
    clear_btn = tk.Button(
        frame,
        text="Clear",
        width=8,
        command=lambda: fun.clear(root),
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


# ----Login Section----


def login_user(
    root, username, passwd, user, check_username, current_user, task_num_list, today
):

    # if the username and the password is correct, proceed.
    if username in user and passwd == user[username]:
        # messagebox.showinfo(title="Success", message="Access granted!")

        # Closes the Login window
        root.destroy()
        main.menu(username, check_username, current_user, task_num_list, today)

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
