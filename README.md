# Capstone Project 19 - Task Manager

<sub>A bootcamp project</sub>

### Table of Contents

1. [Introduction](#introduction)
2. [Project Description](#project-description)
3. [How to use the project](#project-use)
4. [Conclusion](#conclusion)
5. [References](#references)

## 1. Introduction <a name="introduction"></a>

This project was originally a bootcamp task that ran on the console. I wanted to create a GUI, using Tkinter, so I would not have to use the console. The objective of the task was to create a task manager program for a small business to help them manage the tasks of their employees.

## 2. Project Description <a name="project-description"></a>

The project, as stated in the introduction, is a task manager used to help a small business manage tasks of their employees. It allows the user to register new users, assign tasks to them, view tasks, update tasks, generate overviews, and see statistics.

Two files were given, user.txt and tasks.txt. The user.txt file contains the usernames and passwords of the users, one username and password per line. The format of the contents the usernames and password. The tasks.txt file contains a list of tasks assigned to their employees. Each task, in the tasks.txt file, consists of the following:

- The person assigned to the tasks (username).
- The title of the task.
- The description of the task.
- The date the task was given to the user.
- The date the task is due.
- The completion status of the task, 'Yes' - complete and 'No' - incomplete.

## 3. How to run the project?

To run the project you will need to clone the repo to your machine or download a zip file. You can find the either installation options from the dropdown list called code for the repo url or the option to download the zip at the top right corner, next to the _About_ section. Once you have cloned or unzipped the project, you will need to use an IDE, or an integrated development environment, such as Visual Studio Code (VS Code) to run the code. To ensure the program runs install the following:

- Tkinter
- Matplotlib
- tkcalendar
- numpy

<p align="center">
    <img src = "Images/installation_methods.PNG" alt ="Screenshot of options to download project">
</p>

## 4. How to use the project? <a name="project-use"></a>

When you run the program, it will first check if both the tasks.txt and user.txt exist. If the files exist, the program will read the user.txt file and import all the data into a dictionary, i.e., username: password. Once the list of usernames and passwords is stored in a dictionary. When the program has stored the list od usernames and passwords do the following:

- Step 1: Login by entering username and password (check the user.txt file).
- Step 2: Once logged in you will see a list of options, this will differ depending on the user. If the user is admin will see more options than other users. Look at the images below to see the difference.
- Step 3: Click on any of the five (for admin) or three buttons (for other users), they will allow to to register new users, create new tasks, view all tasks, tasks assigned to current user, or to view statistics. Clicking any of this buttons, with the exeception of Close, will generate widets on the right.
  - Register user: allows the admin to register new users. Enter the new user's username and password. You will need to confirm the password, then click Submit. The program will check if there username does not, and it checks if the password and confirm password is the same. If the username exists or if the passwords don't match, an error message will display. The Clear button clears the text boxes.
  - Add task: allows users to add new tasks. You are required to enter the title of the task, select the user, enter the description of the task, and select the due date of the task. Once done click Submit. Clear resets the selection (not working yet).
  - View all tasks: allows the user to view all tasks assigned to all registered users. The Generate report button, as the name states, generates two text files, task_overview.txt and user_overview.txt. Click this button to generate both files, they will be used for statitics function.
  - View my taks: will only display the tasks assigned to current logged in user. The user is able to update any tasks assigned to them by select the task number (do this twice, the first time it does not work). Once you have selected the task you want to update, the program fills in the rest of the widgets with the rest of the data, for example, if admin was to select a tasks assigned to them, it will fill in the assinged user, the title of the tasks, the description, the task status, and the due date. Admin could change the assigned user, the title of the task, description, task status, or the due date. When they are done manking these changes the admin clicks on the Update button to update the task and refreshes the list on the right to show the changes made by admin. If the user changes the assigned user that specific task no longer appears on the current user's list, click on View all tasks to see if it was assigned to the new user.
  - Statistics: diplays user and task overview reports. To display the report, click on View all tasks, then click on Generate report button to generate the text files. The textbox displays the information stored in the user_overview.txt and task_overview.txt files, such as the total number of tasks created, total number of incomplete and complete tasks, etc. The Plot graph button plots a bar chart that displays the number of complete and incomplete tasks by users.
- Step 4: When you have done, close the program.

## 4. Conclusion<a name="conclusion"></a>

## 5. References <a name="references"></a>

- HyperionDev - Software Engineering Bootcamp: Level 1 Capstone Project 19
- [Adding captions to images](https://stackoverflow.com/questions/19331362/using-an-image-caption-in-markdown-jekyll)
