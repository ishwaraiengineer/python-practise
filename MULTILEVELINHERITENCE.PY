#MULTILEVEL INHERITANCE

class Father:
    def fat1(self):
        print("My father")


class Mother:
    def house(self):
        print("My Mother")


class Child(Father, Mother):
    def details(self):
        print("I am child")


# Object creation
c = Child()
c.fat1()
c.house()
c.details()


# ---------------- Multilevel Inheritance ----------------

class Grandfather:
    def house(self):
        print("My Grandfather is our House Owner")


class Father(Grandfather):
    def car(self):
        print("My father has a car")


class Child(Father):
    def study(self):
        print("I am learning Python")


# Object creation
c = Child()
c.house()
c.car()
c.study()