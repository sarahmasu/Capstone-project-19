# =============Libraries=============
import tkinter as tk
from tkinter import ttk
import Scripts.register_gui as reg
import Scripts.add_tasks_gui as add
import Scripts.view_tasks_gui as view
import Scripts.stats_gui as stat
import Scripts.functions as fun

# =============GUI Section=============

# ----Menu Section----


def menu(username, check_username, current_user, task_num_list, today):

    menu_win = tk.Tk()
    menu_win.title("Task Manager")
    menu_win.geometry('900x600') #wxh
    menu_win.configure(bg="#333333")
    menu_win.resizable(0,0)

    height = menu_win.winfo_height()
    width = menu_win.winfo_width()

    # print(f"Screen width x height = {width} x {height}\n")

    # ----Frames/Canvas-----
    main_frame = tk.Frame(menu_win, bg="#333333")
    menu_frame = tk.Frame(main_frame, bg="#333333", width=150, height=800)
    side_frame = tk.Frame(main_frame, bg="#333333", width=650, height=800)

    title_lbl = tk.Label(
        menu_frame,
        text=f"Welcome, {username}",
        bg="#333333",
        fg="#46a094",
        font=("Arial", 18),
    )

    menu_lbl = tk.Label(
        menu_frame,
        text="Select one of the following options:",
        bg="#333333",
        fg="#ffffff",
        font=("Arial", 15),
    )

    # Options for "admin"
    if username == "admin":

        reg_btn = tk.Button(
            menu_frame,
            text="Register user",
            bg="#333333",
            fg="#ffffff",
            width=10,
            font=("Arial", 11),
            command=lambda: reg.register(side_frame),
        )

        add_btn = tk.Button(
            menu_frame,
            text="Add task",
            bg="#333333",
            fg="#ffffff",
            width=10,
            font=("Arial", 11),
            command=lambda: add.add_task(side_frame, check_username, today),
        )

        va_btn = tk.Button(
            menu_frame,
            text="View all tasks",
            bg="#333333",
            fg="#ffffff",
            width=10,
            font=("Arial", 11),
            command=lambda: view.view_tasks(
                side_frame,
                username,
                va_btn.cget("text"),
                current_user,
                task_num_list,
                check_username,
                today,
            ),
        )

        vm_btn = tk.Button(
            menu_frame,
            text="View my tasks",
            bg="#333333",
            fg="#ffffff",
            width=10,
            font=("Arial", 11),
            command=lambda: view.view_tasks(
                side_frame,
                username,
                vm_btn.cget("text"),
                current_user,
                task_num_list,
                check_username,
                today,
            ),
        )

        stats_btn = tk.Button(
            menu_frame,
            text="Statistics",
            bg="#333333",
            fg="#ffffff",
            width=10,
            font=("Arial", 11),
            command=lambda: stat.stats(side_frame),
        )

        clear_frame_btn = tk.Button(
            menu_frame,
            text="Clear frame",
            bg="#333333",
            fg="#ffffff",
            width=15,
            font=("Arial", 10),
            command=lambda: fun.clear_frame(side_frame),
        )

        close_btn = tk.Button(
            menu_frame,
            text="Close",
            bg="#333333",
            fg="#ffffff",
            width=10,
            font=("Arial", 11),
            command=menu_win.destroy,
        )

        # Grids
        title_lbl.grid(row=0, column=0, columnspan=2, pady=25, sticky="news")
        menu_lbl.grid(row=1, column=0, pady=5, sticky="w")

        reg_btn.grid(row=2, column=0, pady=5, padx=5, sticky="ew")
        add_btn.grid(row=3, column=0, pady=5, padx=5, sticky="ew")
        va_btn.grid(row=4, column=0, pady=5, padx=5, sticky="ew")
        vm_btn.grid(row=5, column=0, pady=5, padx=5, sticky="ew")
        stats_btn.grid(row=6, column=0, pady=5, padx=5, sticky="ew")

        close_btn.grid(row=7, column=0, pady=20, padx=5, sticky="ew")

    # Options for other users
    else:

        add_btn = tk.Button(
            menu_frame,
            text="Add task",
            bg="#333333",
            fg="#ffffff",
            width=10,
            font=("Arial", 11),
            command=lambda: add.add_task(side_frame, check_username, today),
        )

        va_btn = tk.Button(
            menu_frame,
            text="View all tasks",
            bg="#333333",
            fg="#ffffff",
            width=10,
            font=("Arial", 11),
            command=lambda: view.view_tasks(
                side_frame,
                username,
                va_btn.cget("text"),
                current_user,
                task_num_list,
                check_username,
                today,
            ),
        )

        vm_btn = tk.Button(
            menu_frame,
            text="View my tasks",
            bg="#333333",
            fg="#ffffff",
            width=10,
            font=("Arial", 11),
            command=lambda: view.view_tasks(
                side_frame,
                username,
                vm_btn.cget("text"),
                current_user,
                task_num_list,
                check_username,
                today,
            ),
        )

        gen_report_btn = tk.Button(
            menu_frame,
            text="Generate Report",
            bg="#333333",
            fg="#ffffff",
            width=10,
            font=("Arial", 11),
            command=lambda: fun.generate_report(check_username),
        )

        close_btn = tk.Button(
            menu_frame,
            text="Close",
            bg="#333333",
            fg="#ffffff",
            width=10,
            font=("Arial", 11),
            command=menu_win.destroy,
        )

        # Grids
        title_lbl.grid(row=0, column=0, columnspan=2, pady=25, sticky="news")
        menu_lbl.grid(row=1, column=0, pady=5)

        add_btn.grid(row=3, column=0, pady=5, padx=10, sticky="ew")
        va_btn.grid(row=4, column=0, pady=5, padx=10, sticky="ew")
        vm_btn.grid(row=5, column=0, pady=5, padx=10, sticky="ew")

        close_btn.grid(row=7, column=0, pady=20, padx=5, sticky="ew")

    # ----Frame/Canvas placement----
    # +++Pack+++
    """ 
    main_frame.pack(side="top", fill="both")
    menu_frame.pack(side="left", padx=10, pady=5, fill="both")
    side_frame.pack(side="left", padx=10, pady=5, fill="both")
    widget_frame.pack(side="left", fill='both' ) 
    """

    # +++Grid+++
    # Outer frame
    main_frame.grid(row=0, column=0,padx=10, sticky='news')

    # Inner frame
    menu_frame.grid(row=0, column=0, padx=15, sticky="nw")
    side_frame.grid(row=0, column=1, padx=15, sticky="new")
    #side_frame.configure(width=600)

    menu_win.mainloop()

    

# ====References====
"""
    - Helped with adding multiple frames in one window:
      https://www.pythonguis.com/faq/pack-place-and-grid-in-tkinter/
"""
