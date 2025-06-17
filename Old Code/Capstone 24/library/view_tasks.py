# ===Explanation of Function====
"""
The view_all function allows the user to view all tasks that have been
assigned.
The program will read the task.txt file:
    - split and strip the data into smaller
      parts
    - assign the split data into variables
    - print them into the appropriate format, making it easier for the
      user to read.

 Example of the format:
 _________________________________________________
 Task:                     Assign initial tasks
 Assigned to:              admin
 Date assigned:            10 Oct 2019
 Date due:                 25 oct 2019
 Task complete?            No

 Task description:
    Use task_manager.py to assign each team member with appropriate tasks
_________________________________________________
"""


# ===End of Explanation===
def view_all():
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

            # Print the output similar to output 2
            print("_________________________________________________\n")

            print(f"Task:\t\t\t{ title :>9}")
            print(f"Assigned to: \t\t{assigned_user :>6}")
            print(f"Date assigned: \t\t{assigned_date :>3}")
            print(f"Date due: \t\t{due_date :>3}")
            print(f"Task complete? \t\t{complete_task}")
            print(f"Task description:\n {description}")

            print("_________________________________________________\n")


# ===Explanation of Function====
"""
    The view_mine function displays the task assigned to the user.
    The program also allows the user to edit their task:
        - The program will request the user to enter the number 
          assigned to the task (-1 to cancel).
        - If the user selects the specific task they wish to edit,
          the progeram should ask the user if they wish to mark the
          task as complete.
        - The program should also ask if they wish to assign the task
          to someone else or to change the due date of the task (The 
          task can only be edited if it has not been completed).
        - Update the edited task in the task list.
"""
# ===End of Explanation===


def view_mine(username, check_username):
    current_user = []
    current_user.clear()

    # Read the task.txt file
    with open("tasks.txt", "r", encoding="utf-8") as read_my_tasks:
        lines = read_my_tasks.readlines()
        count = 1
        # Iterate through task.txt file
        for count, line in enumerate(lines, start=1):
            # Split the lines where there is a comma and a space
            split_lines = line.split(", ")

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
                print("_________________________________________________\n")
                print(f"{count}")
                print(f"Task: \t\t\t{my_title :>10}")
                print(f"Assigned to: \t\t{my_username :>5}")
                print(f"Date assigned: \t\t{my_assigned_date :>3}")
                print(f"Date due: \t\t{my_due_date :>3}")
                print(f"Task complete? \t\t{my_complete_task}")
                print(f"Task description:\n {my_description}")

                print("_________________________________________________\n")

                current_str = (
                    f"{count}, {my_username}, {my_title}, "
                    f"{my_description}, {my_assigned_date}, {my_due_date}, {my_complete_task}"
                )

                current_user.append(current_str)

    task_num = int(input("Enter the task number you wish to edit (-1 to cancel): "))
    try:
        for my_user in current_user:
            data = my_user.strip().split(", ")

            count = data[0]
            my_username = data[1]
            my_title = data[2]
            my_description = data[3]
            my_assigned_date = data[4]
            my_due_date = data[5]
            my_complete_task = data[6]

            # If user enters -1, go back to menu
            if task_num == -1:
                break

            # If the user enters the number from the list
            # program prints the correct value.
            elif task_num == int(count):
                print("_________________________________________________\n")

                print(task_num)
                print(f"Task: \t\t\t{my_title :>10}")
                print(f"Assigned to:\t\t{my_username :>5}")
                print(f"Date assigned: \t\t{my_assigned_date :>3}")
                print(f"Date due: \t\t{my_due_date :>3}")
                print(f"Task complete? \t\t{my_complete_task}")
                print(f"Task description:\n {my_description}")

                print("_________________________________________________\n")

                # User must confirm whether or not they wish to mark the task as complete
                mark_complete = input(
                    "\nWould you like to the aforemention task as complete (yes/no): "
                ).lower()

                # if yes the task will be marked as complete
                # and the the task.txt file will be updated.
                if mark_complete == "yes":
                    my_complete_task = "Yes"

                    with open("tasks.txt", "r", encoding="utf-8") as update_line:
                        lines = update_line.readlines()
                        count = int(count)
                        lines[count - 1] = (
                            f"{my_username}, {my_title}, {my_description}, "
                            f"{my_assigned_date}, {my_due_date}, {my_complete_task}\n"
                        )

                    with open("tasks.txt", "w", encoding="utf-8") as update_line:
                        update_line.writelines(lines)
                        view_all()

                # If the user decides they do not want to mark the task as complete,
                # but wish to assign the task to another user or to change the due date.
                elif mark_complete == "no":
                    select_edt = input(
                        "\nWould you like to assign a different user to the task or change the due date (user/due date): "
                    ).lower()

                    # If the user decides to change re-assign the task, the enter the name a
                    # user they want to assign the task to.
                    if select_edt == "user":
                        user_edit = input(
                            "Enter the user you would like to re-assign the task to: "
                        ).lower()

                        # Checks if the username exists, if not re-enter an existing username.
                        if user_edit in check_username:
                            with open(
                                "tasks.txt", "r", encoding="utf-8"
                            ) as update_line:
                                lines = update_line.readlines()
                            count = int(count)
                            my_username = user_edit
                            lines[count - 1] = (
                                f"{my_username}, {my_title}, {my_description}, "
                                f"{my_assigned_date}, {my_due_date}, {my_complete_task}\n"
                            )

                            with open(
                                "tasks.txt", "w", encoding="utf-8"
                            ) as update_line:
                                update_line.writelines(lines)

                        else:
                            while user_edit not in check_username:
                                user_edit = input(
                                    "That user does not exist! Re-enter the user you wish to re-assign the task to: "
                                ).lower()
                                count = int(count)
                                if user_edit in check_username:
                                    with open(
                                        "tasks.txt", "r", encoding="utf-8"
                                    ) as update_line:
                                        lines = update_line.readlines()

                                    my_username = user_edit
                                    lines[count - 1] = (
                                        f"{my_username}, {my_title}, {my_description}, "
                                        f"{my_assigned_date}, {my_due_date}, {my_complete_task}\n"
                                    )

                                    with open(
                                        "tasks.txt", "w", encoding="utf-8"
                                    ) as update_line:
                                        update_line.writelines(lines)

                                print("User updated!")
                                break

                    # If the user decides to change the due date of the task,
                    # they will be asked enter a new date (dd Mon YY) and the
                    # new date will replace the old date in the tasks.txt file.
                    elif select_edt == "due date":
                        change_date = input("Enter the new due date (dd Mon YYYY): ")
                        count = int(count)
                        with open("tasks.txt", "r", encoding="utf-8") as update_line:
                            lines = update_line.readlines()

                        my_due_date = change_date
                        lines[count - 1] = (
                            f"{my_username}, {my_title}, {my_description}, "
                            f"{my_assigned_date}, {my_due_date}, {my_complete_task}\n"
                        )

                        with open("tasks.txt", "w", encoding="utf-8") as update_line:
                            update_line.writelines(lines)

                        print("Due date updated!")

                # If the user does not enter user or no, the program will loop
                # until they enter either one.
                else:
                    count = int(count)
                    while mark_complete != "yes" or mark_complete != "no":
                        print("Oops, incorrect input!")
                        mark_complete = input(
                            "Please confirm if you would like to mark the task as complete (yes/no): "
                        ).lower()

                        if mark_complete == "yes":
                            my_complete_task = "Yes"

                            with open(
                                "tasks.txt", "r", encoding="utf-8"
                            ) as update_line:
                                lines = update_line.readlines()

                            lines[count - 1] = (
                                f"{my_username}, {my_title}, {my_description}, "
                                f"{my_assigned_date}, {my_due_date}, {my_complete_task}\n"
                            )

                            with open(
                                "tasks.txt", "w", encoding="utf-8"
                            ) as update_line:
                                update_line.writelines(lines)
                                view_all()
                            break

                        elif mark_complete == "no":
                            count = int(count)
                            select_edt = input(
                                "\nWould you like to assign a different user to the "
                                "task or change the due date (user/due date): "
                            ).lower()

                            if select_edt == "user":
                                user_edit = input(
                                    "Enter the user you would like to re-assign the task to: "
                                ).lower()

                                if user_edit in check_username:
                                    with open(
                                        "tasks.txt", "r", encoding="utf-8"
                                    ) as update_line:
                                        lines = update_line.readlines()

                                    my_username = user_edit
                                    lines[count - 1] = (
                                        f"{my_username}, {my_title}, {my_description}, "
                                        f"{my_assigned_date}, {my_due_date}, {my_complete_task}\n"
                                    )

                                    with open(
                                        "tasks.txt", "w", encoding="utf-8"
                                    ) as update_line:
                                        update_line.writelines(lines)

                                else:
                                    while user_edit not in check_username:
                                        user_edit = input(
                                            "That user does not exist! Re-enter the user you wish to re-assign the task to: "
                                        ).lower()

                                        if user_edit in check_username:
                                            with open(
                                                "tasks.txt", "r", encoding="utf-8"
                                            ) as update_line:
                                                lines = update_line.readlines()

                                            my_username = user_edit
                                            lines[count - 1] = (
                                                f"{my_username}, {my_title}, {my_description}, "
                                                f"{my_assigned_date}, {my_due_date}, {my_complete_task}\n"
                                            )

                                            with open(
                                                "tasks.txt", "w", encoding="utf-8"
                                            ) as update_line:
                                                update_line.writelines(lines)

                                            print("User updated!")
                                            break

                            elif select_edt == "due date":
                                change_date = input(
                                    "Enter the new due date (dd Mon YYYY): "
                                )

                                with open(
                                    "tasks.txt", "r", encoding="utf-8"
                                ) as update_line:
                                    lines = update_line.readlines()
                                count = int(count)
                                my_due_date = change_date
                                lines[count - 1] = (
                                    f"{my_username}, {my_title}, {my_description}, "
                                    f"{my_assigned_date}, {my_due_date}, {my_complete_task}\n"
                                )

                                with open(
                                    "tasks.txt", "w", encoding="utf-8"
                                ) as update_line:
                                    update_line.writelines(lines)

                                print("Due date updated!")
                                break
    except ValueError:
        print("Invalid input, please enter a valid integer.")
