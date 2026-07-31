student = {}

roll = int(input("enetr roll number"))
name = input("enetr name")
age = int(input("enetr age"))
course = input(" enter course name")

math = int(input("enter your math marks"))
english = int(input("enter your english marks"))
science = int(input("enter your science marks"))

student[roll] = {
    "name": name,
    "age": age,
    "course": course,
    "marks": {
        "math": math,
        "english": english,
        "science": science
    }

}

for key, values in student.items():
    print(key, ":" , values)
    