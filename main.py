# This is my first python project.
import file_handler
import student
students = file_handler.load_students()


def add_student():
    """Add a new student to the in-memory list."""
    student_id = input("Enter Student ID: ").strip()
    if student_id == "":
        print("Student ID cannot be empty. Please try again.")
        return
    found = False
    for student_obj in students:
        if student_obj.student_id == student_id:
            found = True
            break
    if found:
        print("Student ID already exists. Please try again.")
        return
    name = input("Enter Name: ").strip()
    if name == "":
        print("Name cannot be empty. Please try again.")
        return
    age = int(input("Enter Age: ").strip())
    if age <= 0:
        print("Age must be a positive integer. Please try again.")
        return
    branch = input("Enter Branch: ").strip()
    if branch == "":
        print("Branch cannot be empty. Please try again.")
        return
    cgpa = float(input("Enter CGPA: ").strip())
    if cgpa < 0.0 or cgpa > 10.0:
        print("CGPA must be between 0.0 and 10.0. Please try again.")
        return
    new_student = student.Student(student_id, name, age, branch, cgpa)
    students.append(new_student)
    print("Student added successfully!")


def display_students():
    """Display all students currently stored in memory."""
    if len(students) == 0:
        print("No students found.")
    else:
        print("\n---STUDENT DETAILS---")
        for student_obj in students:
            student_obj.display()


def search_student(student_id=None, student_name=None):
    """Search for a student by their ID or name and display their details."""
    print("---Search Student---", "\n1. Search by ID", "\n2. Search by Name")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        student_id = input("Enter Student ID to search: ").strip()
        for student_obj in students:
            if student_obj.student_id == student_id:
                print("Student found:")
                student_obj.display()
                return student_obj
        print("Student not found")
        return None

    if choice == "2":
        student_name = input("Enter Student Name to search: ").strip()
        if student_name == "":
            print("Name cannot be empty. Please try again.")
            return None

        matches = []
        search_term = student_name.casefold()
        for student_obj in students:
            if search_term in student_obj.name.casefold():
                matches.append(student_obj)

        if matches:
            print("Student found:")
            for student_obj in matches:
                student_obj.display()
            return matches

        print("Student not found")
        return None

    print("Invalid choice. Please try again.")
    return None


def delete_student(student_id):
    """Delete a student by their ID from the in memory list.

    Args:
        student_id: The unique student ID to delete.

    Returns:
        The matching student object if found and deleted; otherwise, None.
    """
    for student_obj in students[:]:
        if student_obj.student_id == student_id:
            students.remove(student_obj)
            file_handler.save_students(students)
            print("Student deleted successfully!")
            return student_obj

    print("Student not found")
    return None


def update_student(student_id):
    """Update a student's details by their ID.

    Args:
        student_id: The unique student ID to update.

    Returns:
        The updated student object if found; otherwise, None.
    """
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


def sort_students():
    if len(students) == 0:
        print("No students found.")
    else:
        print("\n---SORT STUDENTS---")
        print("\nSort By:",
              "\n1. Student ID (Ascending)",
              "\n2. Student ID (Descending)",
              "\n3. Name (A-Z)",
              "\n4. Name (Z-A)"
              "\n5. Age (Youngest - Oldest)",
              "\n6. Age (Oldest - Youngest)",
              "\n7. Branch (Ascending - Descending)",
              "\n8. Branch (Descending- Ascending)",
              "\n9. CGPA (Hghest - lowest)",
              "\n10. CGPA (Lowest - Highest)")
        input_choice = input("Enter your choice: ").strip()
        if input_choice == "1":
            students.sort(key=lambda x: x.student_id)
        elif input_choice == "2":
            students.sort(key=lambda x: x.student_id, reverse=True)
        elif input_choice == "3":
            students.sort(key=lambda x: x.name)
        elif input_choice == "4":
            students.sort(key=lambda x: x.name, reverse=True)
        elif input_choice == "5":
            students.sort(key=lambda x: x.age)
        elif input_choice == "6":
            students.sort(key=lambda x: x.age, reverse=True)
        elif input_choice == "7":
            students.sort(key=lambda x: x.branch)
        elif input_choice == "8":
            students.sort(key=lambda x: x.branch, reverse=True)
        elif input_choice == "9":
            students.sort(key=lambda x: x.cgpa)
        elif input_choice == "10":
            students.sort(key=lambda x: x.cgpa, reverse=True)
        else:
            print("Invalid choice. Please try again.")
            return
        print("Students sorted successfully!")
        display_students()


def display_topper():
    """Display the student with the highest CGPA."""
    if len(students) == 0:
        print("No students found.")
    else:
        topper = []
        for student_obj in students:
            if not topper or student_obj.cgpa > topper[0].cgpa:
                topper = [student_obj]
            elif student_obj.cgpa == topper[0].cgpa:
                topper.append(student_obj)
        print("\n---TOPPER DETAILS---")
        for student_obj in topper:
            student_obj.display()
        return topper


def student_statistics():
    """Display statistics about the students."""
    if len(students) == 0:
        print("No students found.")
    else:
        total_students = len(students)
        average_age = sum(
            student_obj.age for student_obj in students) / total_students
        average_cgpa = sum(
            student_obj.cgpa for student_obj in students) / total_students
        highest_cgpa = max(students, key=lambda x: x.cgpa)
        lowest_cgpa = min(students, key=lambda x: x.cgpa)
        print("\n---STUDENT STATISTICS---")
        print(f"Total Students: {total_students}")
        print(f"Average Age: {average_age:.0f}")
        print(f"Average CGPA: {average_cgpa:.1f}")
        print(f"Highest CGPA: {highest_cgpa.cgpa}")
        print(f"Lowest CGPA: {lowest_cgpa.cgpa}")


# -----------------------------------------------------------------------------------------
while True:
    print("\n---Student Management System---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Save Students")
    print("4. Search Student")
    print("5. Delete Student")
    print("6. Update Student")
    print("7. Sort Students")
    print("8. Display Topper")
    print("9. Student Statistics")
    print("10. Exit")

    choice = input("Enter your choice: ").strip()
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        file_handler.save_students(students)
        print("Students saved successfully!")
    elif choice == "4":
        search_student()
    elif choice == "5":
        delete_student(input("Enter Student ID to delete:").strip())
    elif choice == "6":
        update_student(input("Enter Student ID to update:").strip())
    elif choice == "7":
        sort_students()
    elif choice == "8":
        display_topper()
    elif choice == "9":
        student_statistics()
    elif choice == "10":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

    print("------------------------------")
