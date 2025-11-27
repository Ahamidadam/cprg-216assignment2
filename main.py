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
