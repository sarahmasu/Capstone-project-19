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