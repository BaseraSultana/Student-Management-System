
"""Handle saving and loading student records."""
import student


def save_students(students):
    """Save student records to students.txt."""
    with open("students.txt", "w", encoding="utf-8") as file:
        for student_obj in students:
            file.write(
                f"{student_obj.student_id},{student_obj.name},{student_obj.age},{student_obj.branch},{student_obj.cgpa}\n")


def load_students():
    """
    Loads student data from 'students.txt' and returns a list of Student objects.
    Returns an empty list if the file does not exist.
    """
    loaded_students = []
    try:
        with open("students.txt", "r", encoding="utf-8") as file:
            for line in file:
                student_id, name, age, branch, cgpa = line.strip().split(",")
                loaded_students.append(student.Student(
                    student_id, name, int(age), branch, float(cgpa)))

    except FileNotFoundError:
        print("No saved student data found.")

    return loaded_students
