import json

class Student:
    def __init__(self, name, student_id, age):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.grades = []

    def add_grades(self, grade):
        self.grades.append(grade)

    def average(self ):
        average = sum(self.grades) / len(self.grades)
        return average

    def min_max(self):
        minimum = self.grades[0]
        maximum = self.grades[0]
        for grade in self.grades:
            if grade < minimum:
                minimum = grade
            elif grade > maximum:
                maximum = grade
        return minimum,maximum 


class Classroom:

    def __init__(self):
        self.class_student = {}

    def add_students(self, student):
        self.class_student[student.name] = student

    def get_report(self):
        report = {}
        for name, student in self.class_student.items():
            minimum, maximum = student.min_max()
            report[name] = {
                'age': student.age,
                'student_id': student.student_id,
                'grades': student.grades,
                'average': student.average(),
                'minimum': minimum,
                'maximum': maximum
            }
        return report

    def print_report(self):
        report = self.get_report()
        print(json.dumps(report, indent=2))


def main():
    classroom = Classroom()
    while True:
        student_name = input("please enter the name of the student or enter done to exit : ").lower().strip()
        if student_name == 'done':
            break
        while True:
            try:
                student_id = int(input(f"please enter the student id of {student_name}: " ).strip())
                break
            except ValueError:
                print("please enter a valid student id")

        
        while True:
            try:
                student_age = int(input(f"please enter the age of {student_name} :  ").strip())
                break
            except ValueError:
                print("please enter a valid age")
        new_student = Student(student_name, student_id, student_age)

        while True:
            try:
                grades = input(f"enter the grades of {student_name} or enter done to exit:  ").lower().strip()
                if grades == "done":
                    break
                grades = int(grades)
                new_student.add_grades(grades)
            except ValueError:
                print("please enter a valid grade ")

        classroom.add_students(new_student)

    classroom.print_report()







main()