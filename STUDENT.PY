class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        

    def display_student(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)


class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(student.name, "added successfully ")

    def show_students(self):
        print("\nSchool Name:", self.school_name)
        print("Student List ")
        for s in self.students:
            print("------------------")
            s.display_student()



s1 = Student("Lucky", 1)
s2 = Student("Rahul", 2)

school = School("ABC Public School")


school.add_student(s1)
school.add_student(s2)

school.show_students()