from datetime import datetime

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
