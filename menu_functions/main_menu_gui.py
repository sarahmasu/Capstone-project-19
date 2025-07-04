# =============Libraries=============
import tkinter as tk
import menu_functions.register_gui as reg
import menu_functions.add_tasks_gui as add
import menu_functions.view_tasks_gui as view
import menu_functions.stats_gui as stat
import menu_functions.functions as fun

# =============GUI Section=============

# ----Menu Section----


def menu(username, check_username, current_user, task_num_list, today):

    menu_win = tk.Tk()
    menu_win.title("Task Manager")
    menu_win.configure(bg="#333333")

    height = menu_win.winfo_screenheight()
    width = menu_win.winfo_screenwidth()

    # print(f"Screen width x height = {width} x {height}\n")
    # ----Frames-----
    menu_frame = tk.Frame(
        menu_win, bg="#333333", width=250, height=500)
    side_frame = tk.Frame(menu_win, bg="#333333")

    title_lbl = tk.Label(
        menu_frame,
        text=f"Welcome, {username}",
        bg="#333333",
        fg="#46a094",
        font=("Arial", 24),
    )

    menu_lbl = tk.Label(
        menu_frame,
        text="Select one of the following options:",
        bg="#333333",
        fg="#ffffff",
        font=("Arial", 15),
    )

    # Options for "admin" and other users
    if username == "admin":

        reg_btn = tk.Button(
            menu_frame,
            text="Register user",
            bg="#333333",
            fg="#ffffff",
            width=15,
            font=("Arial", 10),
            command=lambda: reg.register(side_frame),
        )

        add_btn = tk.Button(
            menu_frame,
            text="Add task",
            bg="#333333",
            fg="#ffffff",
            width=15,
            font=("Arial", 10),
            command=lambda: add.add_task(side_frame, check_username, today),
        )

        va_btn = tk.Button(
            menu_frame,
            text="View all tasks",
            bg="#333333",
            fg="#ffffff",
            width=15,
            font=("Arial", 10),
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
            width=15,
            font=("Arial", 10),
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
            width=15,
            font=("Arial", 10),
            command=lambda: stat.stats(side_frame, check_username),
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

    else:

        add_btn = tk.Button(
            menu_frame,
            text="Add Task",
            bg="#333333",
            fg="#ffffff",
            width=15,
            font=("Arial", 10),
            command=lambda: add.add_task(check_username, today),
        )

        va_btn = tk.Button(
            menu_frame,
            text="View All Tasks",
            bg="#333333",
            fg="#ffffff",
            width=15,
            font=("Arial", 10),
            command=lambda: view.view_tasks(
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
            text="View My Tasks",
            bg="#333333",
            fg="#ffffff",
            width=15,
            font=("Arial", 10),
            command=lambda: view.view_tasks(
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
            width=15,
            font=("Arial", 10),
            command=lambda: fun.generate_report(check_username),
        )

        close_btn = tk.Button(
            menu_frame,
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

        add_btn.grid(row=3, column=0, pady=5, padx=10, sticky="ew")
        va_btn.grid(row=4, column=0, pady=5, padx=10, sticky="ew")
        vm_btn.grid(row=5, column=0, pady=5, padx=10, sticky="ew")

        close_btn.grid(row=9, column=0, pady=20, sticky="ew")

    menu_frame.pack(side="left", padx=10, pady=5, fill="both")
    side_frame.pack(side="right", fill="both", padx=10, pady=5)

    menu_win.mainloop()


# ====References====
"""
    - Helped with adding multiple frames in one window:
      https://www.pythonguis.com/faq/pack-place-and-grid-in-tkinter/
"""
