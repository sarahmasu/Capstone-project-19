# ===Explanation of Function===
"""
        The reg_user function takes the username as an argument.
        A list with, the names of all the usernames created,
        will be used to check if the username already exists.

        If the username exists, the while loop will loop until
        the user enters a username that does not exist in the list.

        If the username does not exist, the function will return the 
        new username.
"""
# ===End of Explanation===


def reg_user(user_name):
    with open("../user.txt", "r", encoding="utf-8") as read:
        find_user = read.readlines()

        list_username = []
        list_username.clear()

        for find in find_user:
            split_lines = find.strip().split(", ")
            list_username.append(split_lines[0])

    if user_name not in list_username:
        add_new_user = user_name
        return add_new_user

    if user_name in list_username:
        while user_name in list_username:
            print(f"{user_name} already exist!")
            add_new_user = input("Please enter a new username: ")

            if add_new_user not in list_username:
                return add_new_user


# ===Explanation of Function===
"""
    The display_stats function, displays the statistics from the reports generated from the
    generate_report function. 
"""
# ===End of Explanation===


def display_stats():
    try:
        with open("task_overview.txt", "r", encoding="utf-8") as read_tasks:
            read = read_tasks.readlines()
            print()
            for lines in read:
                split_lines = lines.strip()
                print(split_lines)
            print("_________________________________________________\n")

        with open("user_overview.txt", "r", encoding="utf-8") as read_users:
            read = read_users.readlines()

            for lines in read:
                strip_lines = lines.strip()
                print(strip_lines)

            print("_________________________________________________\n")
    except FileNotFoundError:
        print(
            "The reports do not exist. First generate the reports, gr on the menu, the program will be able to display them."
        )
