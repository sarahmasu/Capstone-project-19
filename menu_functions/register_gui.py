# =============Libraries=============
import tkinter as tk
import menu_functions.functions as fun

# =============GUI Section=============

# ----Register Function----


def register(frame):

    # Creates a child window
    """reg_win = tk.Toplevel()
    reg_win.title("Register")
    reg_win.config(bg="#333333")
    frame = tk.Frame(reg_win, bg="#333333")"""

    # Clear the frame first
    fun.clear_frame(frame)

    title_lbl = tk.Label(
        frame, text="Registration", bg="#333333", fg="#46a094", font=("Arial", 18)
    )

    reg_label = tk.Label(
        frame,
        text="Please enter the following:",
        bg="#333333",
        fg="#ffffff",
        font=("Arial", 15),
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
        command=lambda: fun.submit_user(
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
        command=lambda: fun.clear(frame),
        bg="#46a094",
        fg="#ffffff",
    )

    # ----Grids----
    title_lbl.grid(row=0, column=0, columnspan=2, pady=25, sticky="news")

    reg_label.grid(row=1, column=0, columnspan=2, pady=5, sticky="w")

    user_lbl.grid(row=2, column=0, pady=5, sticky="w")
    new_user.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    passwd_lbl.grid(row=3, column=0, pady=5, sticky="w")
    new_passwd.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    confirm_lbl.grid(row=4, column=0, pady=5, sticky="w")
    confirm_new_passwd.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    submit_btn.grid(row=5, column=0, pady=5, sticky="e")
    clear_btn.grid(row=5, column=1, pady=5, sticky="w")

    frame.pack()
