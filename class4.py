class Clid:
    def __init__(self, name, age, student_class):
        self.name = name
        self.age = age
        self.student_class = student_class

    def show(self):
        print("Name is:", self.name)
        print("Age is:", self.age)
        print("Class is:", self.student_class)

 
obj = Clid("Lucky", 18, "12th")
obj.show()