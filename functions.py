students = {}    #empty dictionary to store students info

def show_menu(): #display menu options and get user choice
    print("What would you like to do today?")
    print("-Find a student? enter 1")
    print("-edit a student's info using student ID? enter 2")
    print("-Add a new student? enter 3")
    print("-Remove a student? enter 4")
    return input()

def add(students_dict, id, name, gpa, semester): #add a new student
    students_dict[id] = [name, gpa, semester]
    print("Student added")
    print(f"{id}      {name}        {gpa}     {semester}")

def remove(students_dict, id): #remove a student
    if id in students_dict:
        del students_dict[id]
        print("Student removed")
    else:
        print("Student not found")

def edit_name(students_dict, id, new_name): #edit a student's name
    if id in students_dict:
        students_dict[id][0] = new_name
        print(f"Student name modified for the student with id  {id}")
        print(f"Student's new name is  {new_name}")
    else:
        print("Student not found")

def search(students_dict, id): #search for a student by id
    if id in students_dict:
        name, gpa, _ = students_dict[id]
        print("Student found")
        print(f"{id}      {name}        {gpa}")
    else:
        print("Student not found")

def run_add(students_dict): #function to add new students
    while True:
        print("Enter id of the student, followed by the student's information.")
        id = input("id:\n")
        name = input("name:\n")
        gpa = float(input("gpa:\n"))
        semester = input("semester:\n")
        add(students_dict, id, name, gpa, semester)
        again = input("Do you want to add a new student?y(yes)/n(no)\n").lower()
        if again != "y" and again != "yes":
            break

def run_search(students_dict): #function to search for students
    while True:
        id = input("Enter the id of the student. Enter -1 to return to the previous menu\n")
        if id == "-1":
            break
        search(students_dict, id)

def run_edit(students_dict): #function to edit student info
    while True:
        id = input("Enter the id of the student. Enter -1 to return to the previous menu\n")
        if id == "-1":
            break
        new_name = input("Enter the new name of the student\n") 
        edit_name(students_dict, id, new_name)

def run_remove(students_dict): #function to remove students
    while True:
        id = input("Enter id of the student that you want to remove from the students' registry.\nid:\n")
        remove(students_dict, id)
        again = input("Do you want to remove more students?y(yes)/n(no)")
        if again.lower() != "y":
            break
