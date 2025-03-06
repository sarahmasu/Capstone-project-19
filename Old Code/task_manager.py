# =====importing libraries===========
from datetime import date

# ====Login Section====

# Open the user.txt file and read the lines
with open("user.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

    # Store the usernames and passwords to be retrieved later on in the code
    check_username = []
    check_passwd = []

    # Traverse through the file'
    for line in lines:
        # Strip the string of the newline character \n
        # Split the string by the comma and the space ","
        split_lines = line.strip().split(", ")
        check_username.append(split_lines[0])
        check_passwd.append(split_lines[1])

    
    # Create a dictionary to check the user credentials
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
            print("Access denied! Password is incorrect.")

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
                print("Access denied! Password is incorrect.")

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

if username == "admin":
    while True:
        # Present the menu to the user and
        # make sure that the user input is converted to lower case.
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

        elif menu == "a":
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

        elif menu == "va":
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

                    print(f"Task: \t\t\t{ title :>10}")
                    print(f"Assigned to: \t\t{assigned_user :>6}")
                    print(f"Date assigned: \t\t{assigned_date :>3}")
                    print(f"Date due: \t\t{due_date :>3}")
                    print(f"Task complete? \t\t{complete_task}")
                    print(f"Task description:\n {description}")

                    print("_________________________________________________\n")

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
                        print("_________________________________________________\n")

                        print(f"Task: \t\t\t{my_title :>10}")
                        print(f"Assigned to: \t\t{my_username :>6}")
                        print(f"Date assigned: \t\t{my_assigned_date :>3}")
                        print(f"Date due: \t\t{my_due_date :>3}")
                        print(f"Task complete? \t\t{my_complete_task}")
                        print(f"Task description:\n {my_description}")

                        print("_________________________________________________\n")
        
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
    while True:
        # Present the menu to the user and
        # make sure that the user input is converted to lower case.
        menu = input(
            """Select one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
    : """
        ).lower()

        if menu == "r":
            # Allows only user "admin" to add new users
            if username != "admin":
                print("\nOnly admins are allowed to add new users.\n")


        elif menu == "a":
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

        elif menu == "va":
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

                    print(f"Task: \t\t\t{ title :>10}")
                    print(f"Assigned to: \t\t{assigned_user :>6}")
                    print(f"Date assigned: \t\t{assigned_date :>3}")
                    print(f"Date due: \t\t{due_date :>3}")
                    print(f"Task complete? \t\t{complete_task}")
                    print(f"Task description:\n {description}")

                    print("_________________________________________________\n")

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
                        print("_________________________________________________\n")

                        print(f"Task: \t\t\t{my_title :>10}")
                        print(f"Assigned to: \t\t{my_username :>6}")
                        print(f"Date assigned: \t\t{my_assigned_date :>3}")
                        print(f"Date due: \t\t{my_due_date :>3}")
                        print(f"Task complete? \t\t{my_complete_task}")
                        print(f"Task description:\n {my_description}")

                        print("_________________________________________________\n")

        elif menu == "e":
            print("Goodbye!!!")
            exit()

        else:
            print("You have made entered an invalid input. Please try again")
# ======= References ========
# References for lines 25 - 77:
# https://stackoverflow.com/questions/43681377/how-to-make-sure-a-user-inputted-password-matches-the-username-registered-to-tha
# Reference: https://www.programiz.com/python-programming/datetime/current-datetime
# Reference for line 210:
# https://www.geeksforgeeks.org/count-number-of-lines-in-a-text-file-in-python/