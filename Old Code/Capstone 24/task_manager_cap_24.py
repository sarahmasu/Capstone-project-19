# =====importing libraries===========
from library.admin_functions import reg_user, display_stats
from library.standard_functions import *

# =====Dictionaries and Lists=====

# Store the usernames and passwords to be retrieved later on in the code

check_username = []
check_passwd = []

# =====Functions Section======

# Stores the username
username = login(check_username, check_passwd)

# ===== Menu Section =====
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
    gr - generate report
    ds - display statistics
    e - exit
    : """
        ).lower()

        if menu == "r":
            # Allows only user "admin" to add new users
            # Request user to enter a user's username and password
            new_user = input("\nEnter new user's username: ").lower()

            #  Calls the function to checks if username exists
            # and stores the new user name in add_user
            add_user = reg_user(new_user)

            new_passwd = input("Enter new user's password: ").lower()

            # Request the user to re-enter the password
            confirm_new_passwd = input("Confirm password: ").lower()

            # Check whether the passwords match
            # If the passwords match append the new user and their password to the user.txt file
            with open("user.txt", "a", encoding="utf-8") as add_file:
                if new_passwd == confirm_new_passwd:
                    add_file.writelines(f"\n{add_user}, {confirm_new_passwd}")
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
            # Calls the function add_task
            add_task()

        elif menu == "va":
            view_all()

        elif menu == "vm":
            # Calls the function to view all the user's task
            # it also allows the user to edit their task.
            view_mine(username, check_username)

        elif menu == "gr":
            generate_report(check_username)

        elif menu == "ds":
            display_stats()

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
    gr - generate report
    e - exit
    : """
        ).lower()

        if menu == "r":
            # Allows only user "admin" to add new users
            if username != "admin":
                print("\nOnly admins are allowed to add new users.\n")

        elif menu == "a":
            # Calls the function add_task
            add_task()

        elif menu == "va":
            # Calls the function to view all task
            view_all()

        elif menu == "vm":
            view_mine(username, check_username)

        elif menu == "gr":
            generate_report(check_username)

        elif menu == "e":
            print("Goodbye!!!")
            exit()

        else:
            print("You have made entered an invalid input. Please try again")

# ======= References ========
# References for lines 25 - 77:
# https://stackoverflow.com/questions/43681377/how-to-make-sure-a-user-inputted-password-matches-the-username-registered-to-tha
# Reference: https://www.programiz.com/python-programming/datetime/current-datetime

# Count the the occurrence of all the user
# Reference: https://stackoverflow.com/questions/2161752/how-to-count-the-frequency-of-the-elements-in-an-unordered-list

# Reference for line 210:
# https://www.geeksforgeeks.org/count-number-of-lines-in-a-text-file-in-python/

# Increment values of a dictionary at certain keys:
# Reference: https://stackoverflow.com/questions/10654499/removing-duplicate-keys-from-python-dictionary-but-summing-the-values

# Add missing keys and values to a dictionary:
# Reference: https://www.geeksforgeeks.org/python-combine-the-values-of-two-dictionaries-having-same-key/
