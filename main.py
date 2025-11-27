"""

Name: Ngor Ruot 

Date: November 27, 2025

Program Description:

This is the main execution file for the Student Record Program. It displays the menu, takes user input, calls the appropriate functions from functions.py, 
and loops until the user chooses to exit. The program interacts with the shared dictionary 'students' to store student profiles including name, GPA, 
and semester. Inputs come from the keyboard and outputs are printed messages confirming modifications, search results, and program actions.

"""


from functions import *

print("Welcome to the students record program")

while True:
    choice = show_menu()

    if choice == "1":
        run_search(students)
    elif choice == "2":
        run_edit(students)
    elif choice == "3":
        run_add(students)
    elif choice == "4":
        run_remove(students)

    cont = input("What you like to continue(y/yes), or exit the program(n/no)?\n").lower()
    if cont not in ["y", "yes"]:
        break     