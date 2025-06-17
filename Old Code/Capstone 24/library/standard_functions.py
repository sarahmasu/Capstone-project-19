# ====Libraries====
from datetime import date
from datetime import datetime

# ====Login Section====


def login(check_username, check_passwd):
    # Open the user.txt file and read the lines
    with open("user.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

        # Traverse through the file
        for line in lines:
            # Strip the string of the newline character \n
            # Split the string by the comma and the space ","
            split_lines = line.strip().split(", ")
            check_username.append(split_lines[0])
            check_passwd.append(split_lines[1])

        # Create a dictionay to check the user credentials
        user = dict(zip(check_username, check_passwd))

    # Request the user to enter the username
    username = input("Enter the username: ").lower()

    # Check if the username is correct
    if username in check_username:
        # While the username is in the list loop until the user
        # enter the correct password
        while username in check_username:
            passwd = input("Enter the password: ").lower()

            if username in check_username and passwd == user[username]:
                print("Access granted!\n")
                break

            else:
                print("Acccess denied! Password is incorrect.")

    # If the username is incorrect
    else:
        # While the username is incorrect loop until the user
        # enters the correct user name
        while username not in check_username:
            print("Access denied! Incorrect username.")
            username = input("Enter the username: ").lower()

            if username in check_username:
                passwd = input("Enter the password: ").lower()

                if passwd == user[username]:
                    print("Access granted!\n")
                    break

                else:
                    print("Acccess denied! Password is incorrect.")

                    # While the password is incorrect, loop until the correct
                    # password is given
                    while passwd != user[username]:
                        if passwd == user[username]:
                            print("Access granted!\n")
                            break
                        else:
                            passwd = input("Enter the password: ").lower()

            else:
                print("Access denied! Username is incorrect.")
                username = input("Enter the username: ").lower()

    return username


# ===Explanation of Function====
"""
    The add_task allows a user to add a task to themselves or another user:
    - The program first opens the task.txt file to add a task to a user.
    - The program will request the following:
        * Who to assign the task to
        * The title of the task
        * The description of the task
        * The due date of the task
    - The program will assign the current date the task was given.
    - Once all the input has been given the program will then append to
        the task.txt file.
"""
# ===End of Explanation===


def add_task():
    # Append user input and format the output to task.txt
    with open("tasks.txt", "a", encoding="utf-8") as file:
        # Request the user to assign other users tasks, the name of the task,
        # the description and when it's due
        user_task = input("\nEnter the user you want to assign a task to: ")
        task_title = input("Enter the title of the task: ")
        task_description = input("Enter the decription of the task: ")
        task_due_date = input("Enter the due date of the task (dd Mon YYYY): ")

        # Get current date and format it to dd Mon YYYY
        today = date.today()
        current_date = today.strftime("%d %b %Y")

        # The default value of task_complete
        task_complete = "No"

        file.writelines(
            f"\n{user_task}, {task_title}, {task_description}, "
            f"{current_date}, {task_due_date}, {task_complete}"
        )


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


# ===Explanation of Function====
"""
    The generate_report function creates two text files based on the information 
    gathered in the tasks.txt file and the user.txt file.

    The program will generate the task_overview.txt file:
        - Count the total number of tasks
        - Count the total number of complete and incomplete tasks
        - Count the total number of incomplete and overdue tasks
        - Find the percentage of complete and incomplete tasks
        - Find the percentage of incomplete and overdue tasks.
        - Create and write to task_overview.txt file.
    
    The program will generate the user_overview.txt file:
        - Count the total number of users.
        - Count the total number of user that were assigned tasks.
        - Find the percentage of incomplete assigned tasks.
        - Find the percentage of complete assigned tasks.
        - Find the percentage of complete and overdue tasks.
        - Create and write to the user_overview.txt file.
"""
# ===End of Explanation===


def generate_report(check_username):
    # Variables to store the results
    total_overdue_incomplete_task = 0
    total_incomplete_task = 0
    total_complete_task = 0

    count_complete_users = 0
    count_incomplete_users = 0
    count_overdue_user = 0

    # Lists to store the values
    check_list = []
    check_list.clear()

    dup_list = []
    dup_list.clear()

    overdue_list = []
    overdue_list.clear()

    task_list = []
    task_list.clear()

    # Dictionaries to store keys and their values
    tasks_comp_dict = {}
    tasks_comp_dict.clear()

    tasks_incomp_dict = {}
    tasks_incomp_dict.clear()

    check_user_dict = {}
    check_user_dict.clear()

    user_dict = {}
    user_dict.clear()

    due_date_dict = {}
    due_date_dict.clear()

    # Read the task.txt file and retrieve the information from it
    with open("tasks.txt", "r", encoding="utf-8") as read_all_tasks:
        lines = read_all_tasks.readlines()

        total_tasks = len(lines)
        total_users = len(check_username)

        for line in lines:
            split_lines = line.strip().split(", ")

            assigned_user = split_lines[0]
            due_date = split_lines[4]
            complete_task = split_lines[5]

            # Count the number of complete an incomplete tasks
            total_complete_task += complete_task.count("Yes")
            total_incomplete_task += complete_task.count("No")

            today = datetime.today()
            task_due = datetime.strptime(due_date, "%d %b %Y")

            # Counts the incomplete overdue tasks, by comparing the current date to the due date
            if task_due < today:
                total_overdue_incomplete_task += complete_task.count("No")

            # Use the check_list to add the users assigned to a task,
            # then append the non-duplicates to the dup_list.
            check_list.append(assigned_user)
            [
                dup_list.append(assigned_user)
                for assigned_user in check_list
                if assigned_user not in dup_list
            ]

            task_list.append(assigned_user + ", " + complete_task)

            # Count all the complete tasks and incomplete tasks
            # assigned to the users.
            if "Yes" in complete_task:
                count_complete_users += 1
            else:
                count_incomplete_users += 1

            # Count all incomplete and overdue tasks assigned to users
            if task_due < today and "No" in complete_task:
                count_overdue_user += 1
                overdue_list.append(assigned_user + ", " + complete_task)

        # Stores the default values for the users
        for i in check_username:
            check_user_dict[i] = 0

        # Struggled to count the number of users.
        user_dict = {x: check_list.count(x) for x in check_username}

        # Calculate the percentages of assigned tasks to each user
        for key, val in user_dict.items():
            user_dict[key] = round(val / total_users * 100, 2)

        comp_task_list = [sub.replace("Yes", "1") for sub in task_list]
        comp_task_list = [sub.replace("No", "0") for sub in comp_task_list]

        incomp_task_list = [sub.replace("No", "1") for sub in task_list]
        incomp_task_list = [sub.replace("Yes", "0") for sub in incomp_task_list]

        overdue_list = [sub.replace("No", "1") for sub in overdue_list]

        # Add complete tasks to task_comp_dict
        for key in comp_task_list:
            try:
                key = key.strip().split(", ")
                assigned_user = key[0]
                complete_task = key[1]
                tasks_comp_dict[assigned_user] += int(complete_task)
            except:
                tasks_comp_dict[assigned_user] = int(complete_task)

        # Add incomplete tasks to task_incomp_dict
        for key in incomp_task_list:
            try:
                key = key.strip().split(", ")
                assigned_user = key[0]
                complete_task = key[1]

                tasks_incomp_dict[assigned_user] += int(complete_task)
            except:
                tasks_incomp_dict[assigned_user] = int(complete_task)

        for key in overdue_list:
            try:
                key = key.strip().split(", ")
                assigned_user = key[0]
                complete_task = key[1]

                due_date_dict[assigned_user] += int(complete_task)
            except:
                due_date_dict[assigned_user] = int(complete_task)

        # Add missing keys and values to task_comp_dict.
        for key in check_user_dict:
            tasks_comp_dict[key] = check_user_dict[key] + tasks_comp_dict.get(key, 0)

        for key, val in tasks_comp_dict.items():
            tasks_comp_dict[key] = round(val / total_tasks * 100, 2)

        # Add missing keys and values to task_incomp_dict.
        for key in check_user_dict:
            tasks_incomp_dict[key] = check_user_dict[key] + tasks_incomp_dict.get(
                key, 0
            )

        for key, val in tasks_incomp_dict.items():
            tasks_incomp_dict[key] = round(val / total_tasks * 100, 2)

        # Add missing keys and values to due_date_dict
        for key in check_user_dict:
            due_date_dict[key] = check_user_dict[key] + due_date_dict.get(key, 0)

        for key, val in due_date_dict.items():
            due_date_dict[key] = round(val / total_tasks * 100, 2)

        # Calculates the percentage of incomplete and overdue tasks
        percent_incomplete_tasks = (total_incomplete_task / total_tasks) * 100
        percent_overdue_tasks = (total_overdue_incomplete_task / total_tasks) * 100

        # Gets the total number of user and total users assigned to tasks.
        assigned_users = len(dup_list)
        total_assigned_users = assigned_users

        # Prevents the program from dividing by zero,
        # by return 0
        if total_users == 0:
            percent_assigned_complete = 0
        else:
            percent_assigned_users = (total_assigned_users / total_users) * 100

        if total_tasks == 0:
            percent_assigned_complete = 0
            percent_assigned_incomplete = 0
            percent_assigned_incomplete_overdue = 0
        else:
            percent_assigned_complete = (count_complete_users / total_tasks) * 100
            percent_assigned_incomplete = (count_incomplete_users / total_tasks) * 100
            percent_assigned_incomplete_overdue = (
                count_overdue_user / total_tasks
            ) * 100

    # Create two text files, task_overview and user_overview, to write the results to.
    with open("task_overview.txt", "w", encoding="utf-8") as write_task:
        write_task.writelines(
            "Task Overview report\n"
            "_________________________________________________\n"
            f"Total tasks; {total_tasks}\n"
            f"Total complete tasks: {total_complete_task}\n"
            f"Total incomplete tasks: {total_incomplete_task}\n"
            f"Total incomplete and overdue tasks: {total_overdue_incomplete_task}\n"
            f"Percentage of incomplete tasks: {round(percent_incomplete_tasks, 2)}%\n"
            f"Percentage of overdue tasks: {round(percent_overdue_tasks, 2)}%"
        )

    with open("user_overview.txt", "w", encoding="utf-8") as write_user:
        write_user.writelines(
            "User Overview report\n"
            "_________________________________________________\n"
            f"Total users: {total_users}\n"
            f"Total assigned: {total_assigned_users}\n"
            f"Percentage of assigned tasks: {round(percent_assigned_users, 2)}%\n"
            f"Percentage of assigned complete tasks: {round(percent_assigned_complete)}%\n"
            f"Percentage of assigned incomplete tasks: {round(percent_assigned_incomplete, 2)}%\n"
            f"Percentage of assigned overdue tasks: {round(percent_assigned_incomplete_overdue, 2)}%"
            f"\n\nTasks assigned to users\n"
            f"_________________________________________________\n"
        )

        for key, val in user_dict.items():
            write_user.writelines(f"\n{key:5}: {val}%")

        write_user.writelines(
            "\n\nCompleted tasks assigned to users\n"
            "_________________________________________________\n"
        )

        for key, val in tasks_comp_dict.items():
            write_user.writelines(f"\n{key:5}: {val}%")

        write_user.writelines(
            "\n\nIncomplete tasks assigned to users\n"
            "_________________________________________________\n"
        )

        for key, val in tasks_incomp_dict.items():
            write_user.writelines(f"\n{key:5}: {val}%")

        write_user.writelines(
            "\n\nIncomplete and overdue tasks assigned to users\n"
            "_________________________________________________\n"
        )

        for key, val in due_date_dict.items():
            write_user.writelines(f"\n{key:5}: {val}%")

    print("\nUser and Task overview reports generated!\n")
