class Student:
    def __init__(self, student_id, name, age, branch, cgpa):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.branch = branch
        self.cgpa = cgpa

    def display(self):
        print("")
        print("---STUDENT DETAILS---")
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Branch:", self.branch)
        print("CGPA:", self.cgpa)
