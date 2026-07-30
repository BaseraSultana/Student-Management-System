import student


def save_students(students):
    with open("students.txt", "w") as file:
        for student_obj in students:
            file.write(
                f"{student_obj.student_id},{student_obj.name},{student_obj.age},{student_obj.branch},{student_obj.cgpa}\n")


def load_students():
    loaded_students = []
    try:
        with open("students.txt", "r") as file:
            for line in file:
                student_id, name, age, branch, cgpa = line.strip().split(",")
                loaded_students.append(student.Student(
                    student_id, name, int(age), branch, float(cgpa)))

    except FileNotFoundError:
        print("No saved student data found.")

    return loaded_students
