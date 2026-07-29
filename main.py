import student
students = []


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    branch = input("Enter Branch: ")
    cgpa = float(input("Enter CGPA:"))
    new_student = student.Student(student_id, name, age, branch, cgpa)
    students.append(new_student)
    print("Student added successfully!")


def display_students():
    if len(students) == 0:
        print("No students found.")
    else:
        print("\n---STUDENT DETAILS---")
        for student_obj in students:
            student_obj.display()


while True:
    print("\n---Student Management System---")
    print("1. Add STudent")
    print("2. Display Students")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
    print("------------------------------")
