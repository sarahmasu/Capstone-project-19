# Capstone Project 19 - Task Manager

<sub>A bootcamp project</sub>

### Table of Contents

1. [Introduction](#introduction)
2. [How does it work?](#project-description)

   2.1. [Registering Users](#reg_users)

   2.2. [Adding Tasks](#add_tasks)

   2.3. [Viewing Tasks](#view_tasks)

   2.4. [Statistics](#view_stats)

3. [References](#references)

## 1. Introduction <a name="introduction"></a>

This project was originally a bootcamp task that ran on console. I wanted to create a GUI, using Tkinter, so I would not have to use the console. The objective of the task was to create a task manager program for small business to help them manage tasks of their employees.

They gave us two files, user.txt and tasks.txt. The user.txt files contains the username and passwords of the users, one username and password per line. The format of the contents is as follows: username, password.

The tasks.txt file contains a list of tasks assigned to their employees. Each tasks, in the tasks.txt file, consists of the following:

- The person assigned to the tasks (username).
- The title of the task.
- The description of the task.
- The date the task was given to the user.
- The date the task is due.
- The completion status of the task, 'Yes' - complete and 'No' - incomplete.

## 2. How does it work? <a name="project-description"></a>

When you run the program, it will first check if the both the tasks.txt and user.txt exists. If the files exists the program will read the user.txt file import all the data into a dictionary, i.e., username: password. Once the list of usernames and passwords are stored in a dictionary, the Login window will display, enter the username and password to proceed then you will see the main menu.

<p align="center">
    <img src="/Images/Login.PNG" alt="Screenshot of Login window">
</p>
<p align="center">
    <em>Login window</em>
</p>

Once you have logged in, there are two menus, one for admin and one for the other users. The windows share the following functions:

- Add tasks
- View all tasks
- View my tasks

There is two functions exclusive to admin which are:

- Statistics
- Register user

<p align="center">
    <img src="/Images/Main_menu_admin.PNG" alt="Screenshot of Menu window for admin" height = "300" width="450">
    <img src="/Images/Main_menu_users.PNG" alt="Screenshot of Menu window for users" height="300" width="450">
</p>
<p align="center">
    <em>Main menu windows for admin (left) and other users (right).</em>
</p>

### 2.1. Registering new users <a name="reg_users"></a>

This function is available only to admins. When you choose to register a new user, you will be prompted to enter the new user's username and password. Once you confirm their password, the program will open the user.txt file and write the new user and the password to it. Otherwise, it will loop until the admin ensures that the password and the confirmation password are the same. The same applies if the admin enters nothing when prompted to enter a password.

<p align="center">
    <img src="/Images/Register_menu.PNG" alt="Screenshot of Register window" title="Register window.">
</p>
<p align="center">
    <em>Register user window</em>
</p>

### 2.2. Adding a task <a name="add_tasks"></a>

When you choose to add a task, the program will open the tasks.txt file, then prompt the user to enter the title of the task, the task description, when the task is due, and who they wish to assign the task to. The date the task was added will be the current date, and the task will be defaulted to incomplete. All the information will be written to the file.

<p align="center">
    <img src="/Images/Add_task_menu.PNG" alt="Screenshot of Add task window" title="Add Task window.">
</p>
<p align="center">
    <em>Add tasks window</em>
</p>

### 2.3. Viewing tasks <a name="view_tasks"></a>

There are two options when it comes to viewing tasks: view all assigned tasks and tasked assigned to tasks assigned to the current user.

View all assigned tasks reads all the tasks from the tasks.txt file, and view my tasks views all the tasks assigned to the current user.

<p align="centerS">
    <img src="/Images/View_all_tasks_menu.PNG" alt="Screenshot of View all tasks window" width="300" height="450">
    <img src="/Images/View_my_tasks_menu.PNG" alt="Screenshot of View my tasks window" width="300" height="450">
</p>
<p align="center">
    <em>View tasks window for all tasks(left) and current user(right)</em>
</p>

### 2.4. Statistics <a name="view_stats"></a>

This function can only available to admin only. Reads all the information in both tasks.txt and user.txt files. The function counts the total number of users and tasks from both text files and outputs the results.

<p align="center">
    <img src="/Images/Statistics_menu.PNG" alt="Screenshot of Statistics window">
</p>
<p align="center">
    <em>Statistics window</em>
</p>

## 3. References <a name="references"></a>

HyperionDev - Software Engineering Bootcamp: Level 1 Capstone Project 19
