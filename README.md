# Capstone Project 19 - Task Manager

<sub>A bootcamp project</sub>

## Table of Contents

1. [Introduction](#introduction)
2. [Project Description](#project-description)

    2.1. [Registering Users](#reg_users)

    2.2. [Adding Tasks](#add_tasks)

    2.3. [Viewing Tasks](#view_tasks)

    2.4. [Statistics](#view_stats)

3. [References](#references)

This was a bootcamp capstone project I wanted to revisit. I've added the old code, updated code, and the GUI using Tkinter.

## 1. Introduction <a name="introduction"></a>

The focus of this project was to add functionality to a task manager program. The code originally had the menu, and I was tasked to make the menu options functional.

## 2. Project Description <a name="project-description"></a>
You will be prompted to enter a username and password when you run the code. Once the correct username and password are given, a menu will appear:
<p align="center">
    <img src="/Images/Login.PNG" alt="Screenshot of Login window">
</p>

The options are to register new users, add new tasks, view all available tasks, view all tasks of the current user, and view statistics. Registering new users and viewing statistics are reserved for the admin.

<p align="center">
    <img src="/Images/Menu.PNG" alt="Screenshot of Menu window">
</p>

### 2.1. Registering new users <a name="reg_users"></a>
This function is available only to admins. When you choose to register a new user, you will be prompted to enter the new user's username and password. Once you confirm their password, the program will open the user.txt file and write the new user and the password to it. Otherwise, it will loop until the admin ensures that the password and the confirmation password are the same. The same applies if the admin enters nothing when prompted to enter a password.

<p align="center">
    <img src="/Images/Register_menu.PNG" alt="Screenshot of Register window">
</p>

### 2.2. Adding a task <a name="add_tasks"></a>
When you choose to add a task, the program will open the tasks.txt file, then prompt the user to enter the title of the task, the task description, when the task is due, and  who they wish to assign the task to. The date the task was added will be the current date, and the task will be defaulted to incomplete. All the information will be written to the file.

<p align="center">
    <img src="/Images/Add_task_menu.PNG" alt="Screenshot of Add task window">
</p>

### 2.3. Viewing tasks <a name="view_tasks"></a>
There are two options when it comes to viewing tasks: view all assigned tasks and tasked assigned to tasks assigned to the current user.

View all assigned tasks reads all the tasks from the tasks.txt file, and view my tasks views all the tasks assigned to the current user.

<p align="center">
    <img src="/Images/View_all_tasks_menu.PNG" alt="Screenshot of View all tasks window">
</p>

<p align="center">
    <img src="/Images/View_my_tasks_menu.PNG" alt="Screenshot of View my tasks window">
</p>

### 2.4. Statistics <a name="view_stats"></a>
This function can only available to admin only. Reads all the information in both tasks.txt and user.txt files. The function counts the total number of users and tasks from both text files and outputs the results.

<p align="center">
    <img src="/Images/Statistics_menu.PNG" alt="Screenshot of Statistics window">
</p>

## 3. References <a name="references"></a>
HyperionDev - Software Engineering Bootcamp: Level 1 Capstone Project 19
