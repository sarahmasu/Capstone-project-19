from datetime import date

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