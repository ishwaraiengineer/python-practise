
# STUDENT MANAGEMENT SYSTEM

students = {}

while True:
    print("\n STUDENT MANAGEMENT SYSTEM ")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":
        roll = int(input("Enter Roll Number: "))

        if roll in students:
            print("Student already exists!")
        else:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            course = input("Enter Course: ")

            students[roll] = {
                "name": name,
                "age": age,
                "course": course
            }

            print("Student Added Successfully!")

    
    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\n Student Records ")

            for roll, details in students.items():
                print(f"""
Roll No : {roll}
Name    : {details['name']}
Age     : {details['age']}
Course  : {details['course']}
""")

    
    elif choice == "3":
        roll = int(input("Enter Roll Number to Search: "))

        if roll in students:
            details = students[roll]

            print("\nStudent Found")
            print("Name   :", details["name"])
            print("Age    :", details["age"])
            print("Course :", details["course"])

        else:
            print("Student not found!")

    
    elif choice == "4":
        roll = int(input("Enter Roll Number to Update: "))

        if roll in students:
            name = input("Enter New Name: ")
            age = int(input("Enter New Age: "))
            course = input("Enter New Course: ")

            students[roll] = {
                "name": name,
                "age": age,
                "course": course
            }

            print("Student Updated Successfully!")

        else:
            print("Student not found!")

    
    elif choice == "5":
        roll = int(input("Enter Roll Number to Delete: "))

        if roll in students:
            del students[roll]
            print("Student Deleted Successfully!")

        else:
            print("Student not found!")


    elif choice == "6":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Please try again.")