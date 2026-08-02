# This is my first python project.
import file_handler
import student
students = file_handler.load_students()


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


def search_student(student_id):
    for student_obj in students:
        if student_obj.student_id == student_id:
            print("Student found:")
            student_obj.display()
            return student_obj

    print("Student not found")
    return None


def delete_student(student_id):
    for student_obj in students:
        if student_obj.student_id == student_id:
            students.remove(student_obj)
            file_handler.save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found")
    return None


def update_student(student_id):
    for student_obj in students:
        if student_obj.student_id == student_id:
            print("Enter new details (press enter to keep current value):")

            name = (
                input(f"Enter New Name [{student_obj.name}]: ")) or student_obj.name
            age = (
                input(f"Enter New Age [{student_obj.age}]: ")) or student_obj.age
            branch = input(
                f"Enter New Branch [{student_obj.branch}]: ") or student_obj.branch
            cgpa = (
                input(f"Enter New CGPA [{student_obj.cgpa}]: ")) or student_obj.cgpa
            student_obj.name = name
            student_obj.age = int(age)
            student_obj.branch = branch
            student_obj.cgpa = float(cgpa)
            file_handler.save_students(students)
            print("Student details updated successfully!")
            return

    print("Student not found")
    return None


while True:
    print("\n---Student Management System---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Save Students")
    print("4. Search Student")
    print("5. Delete Student")
    print("6. Update Student")
    print("7. Exit")

    choice = input("Enter your choice: ").strip()
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        file_handler.save_students(students)
        print("Students saved successfully!")
    elif choice == "4":
        search_student(input("Enter Student ID to search: ").strip())
    elif choice == "5":
        delete_student(input("Enter Student ID to delete:").strip())
    elif choice == "6":
        update_student(input("Enter Student ID to update:").strip())
    elif choice == "7":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

    print("------------------------------")
