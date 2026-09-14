import time

student_grades = {}    # made an empty dictionary.
print("===================================================================================")
print("                         Students' Grade Management System                         ")     # printed the welcome message.
print("===================================================================================")

def add_student(name, grade):   # add student option completed.
    student_grades[name] = grade
    print(f"Added {name} with grade {grade}")
    
    
def get_student(name):      #get student option completed.
    if name in student_grades:
        print(f"{name}: {student_grades[name]}")
    else:
        print(f"Student {name} not found.")
        
def update_student(name, grade):    # update student option completed.
    if name in student_grades:
        student_grades[name] = grade
        print(f"Updated {name} to grade {grade}")
    else:
        print(f"Student {name} not found.")
        
def delete_student(name):     # delete student option completed.
    if name in student_grades:
        del student_grades[name]
        print(f"Deleted {name}")
    else:
        print(f"Student {name} not found.")
        
def display_all_students():     # display option completed.
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No students found.")
print("\n ================ Welcome to Students' Grades Management System ===============")
time.sleep(1)
print()
print()

        
def main():
    while True:
        print("1. Add Student")
        print("2. Get Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Display All Students")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter student name: ")
            grade = input("Enter student grade: ").upper()
            add_student(name, grade)           
        elif choice == '2':
            name = input("Enter student name: ")
            get_student(name)
        elif choice == '3':
            name = input("Enter student name: ")
            grade = input("Enter new grade: ").upper()
            update_student(name, grade)
        elif choice == '4':
            name = input("Enter student name: ")
            delete_student(name)
        elif choice == '5':
            display_all_students()
        elif choice == '6':    # exiting option completed.
            print("Exiting the program.")
            time.sleep(1)
            print("Thanks for using the Student Grades Management System!")
            print("======================================================")
            time.sleep(1)
            break
        else:
            print("Invalid choice. Please try again.")
        
        time.sleep(1)
        
        
            
main()   # executed the program.
