# ====Import Libraries====
from datetime import date
from Scripts.functions import check_file
from Scripts.login_gui import login

# ====Dictionaries & Lists====

check_username = []
check_passwd = []
current_user = []
task_num_list = []
user = {}

today = date.today()

# ===============Main Function===============

if __name__ == "__main__":
    check_file(check_username, check_passwd, user)
    login(user, check_username, current_user, task_num_list, today)

# ====References====
"""
    Added items to empty user dictionary. Check login section
    - https://www.geeksforgeeks.org/adding-items-to-a-dictionary-in-a-loop-in-python/

    Updating dictionary, see register user method
    - https://www.w3schools.com/python/python_dictionaries_add.asp

    Creating the simple GUI
    - https://www.makeuseof.com/python-login-page-simple-build/
    - https://www.youtube.com/watch?v=MeMCBdnhvQs
    - https://www.w3resource.com/python-exercises/tkinter/python-tkinter-layout-management-exercise-3.php

    Colour palette
    - https://za.pinterest.com/pin/330310953935935490/

    Clearing the widgets:
    - https://www.youtube.com/watch?v=IFcIVl6da5o

    Closing a window, without a button:
    - https://stackoverflow.com/questions/67295637/closing-current-window-when-opening-a-new-window-in-tkinter-python

    Changing the size of buttons:
    - https://www.tutorialspoint.com/how-do-i-change-button-size-in-python-tkinter

    Fixed the closing error for the main menu
    - https://stackoverflow.com/questions/21645716/cannot-invoke-button-command-application-has-been-destroyed

    Fixed an error caused by frame and pack
    - https://stackoverflow.com/questions/23584325/cannot-use-geometry-manager-pack-inside

    Solves the frame issue for TopLevel Widgets
    - https://stackoverflow.com/questions/52950267/tkinter-frame-in-toplevel-displayed-in-parent

    Solves the issue of clearing all entry window
    - https://stackoverflow.com/questions/69866188/python-is-there-a-way-to-clear-all-entry-boxes-in-a-tkinter-ui-in-one-line

    Calendar: installation and creation of gui
    - https://dev.to/zettasoft/how-to-make-a-calendar-using-python-tkinter-4ijj
    - https://www.geeksforgeeks.org/create-a-date-picker-calendar-tkinter/

    Alignment of widgets
    - https://stackoverflow.com/questions/74418639/aligning-entries-buttons-with-tkinter

    Get the text of the button:
    - https://stackoverflow.com/questions/26765218/get-the-text-of-a-button-widget

    Fixed line 465 - TypeError: descriptor 'strftime' for 'datetime.date' objects doesn't apply to a 'str' object:
    - https://stackoverflow.com/questions/30112357/typeerror-descriptor-strftime-requires-a-datetime-date-object-but-received

    Functions of tkCalendar:
    - https://tkcalendar.readthedocs.io/en/stable/Calendar.html

    Fixed date conversion error for search_list:
    - https://stackoverflow.com/questions/25015711/time-data-does-not-match-format

    Removed the search button and adding bindings to chg_task_num_cmbo:
    - https://stackoverflow.com/questions/73238441/tkinter-how-to-pass-arguments-when-comboboxselected-is-bound-to-a-method

    Fixed the issue with import functions from the same folder:
    - https://stackoverflow.com/questions/43865291/import-function-from-a-file-in-the-same-folder

    Added canvas to act as a scrollable frame for bigger guis:
    https://stackoverflow.com/questions/40526496/vertical-scrollbar-for-frame-in-tkinter-python
"""
