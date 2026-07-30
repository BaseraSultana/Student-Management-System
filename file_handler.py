def save_students(students):
    with open("students.txt", "w") as file:
        for student_obj in students:
            file.write(
                f"{student_obj.student_id},{student_obj.name},{student_obj.age},{student_obj.branch},{student_obj.cgpa}\n")
