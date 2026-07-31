students = {}

while True:
    print("press 1 for add student")
    print("press 2  for view all student")
    print("press 3 for update student")
    print("press 4 for search student")
    print("press 5 for delete student")
    print("press 6 for exit")
    
    choice = int(input("press the number : "))
    if choice == 1:
        roll = int(input("enter your roll number"))
        if roll in students:
            print("student already exit")
        else:
            name = input("enter your name: ")
            course = input("enterr your course name: ")
            age = int(input("enter age: "))
            
            students[roll] = {
                "name": name,
                "course": course,
                "age": age
            }
            print(" student added succesfully ")
            
    elif choice == 2:
        if len(students) == 0:
            print ("  no student data found  ")
        else:
            print(" student records ")
            
            
            for roll,details in students.items():
                print(f"""
roll no : {roll}
name : {details['name']}
course : {details['course']}
age : {details['age']}
""")
    elif choice == 3:
        roll = int(input("enter your roll no. to update: "))
        if roll in students:
            name = input("enter  new name : ")
            age = int(input("enter new age : "))
            course = input("enter new course : ")
            
            students[roll] = {
                "name": name,
                "course": course,
                "age": age
            }
            
            print("_____student is updated _____")
        else:
            print("_____student not found______")
    elif choice == 4:
        roll = int(input("enter your roll numner for search : "))
        
        if roll in students:
            details = students[roll]
            
            print("------ student found --------")
            print(" name  :",details["name"])
            print(" course  :",details["course"])
            print(" age  :",details["age"])
        else:
            print("student not found  ")
    
    
    elif choice == 5:
        roll = int(input("enter roll number for deleting : "))
        
        if roll in students:
            del students[roll]
            print("student id is deleted succesfully")
        else:
            print("student not found  ")
            
            
    elif choice == 6:
        print("exit......")
        break
    
    else:
        print("incorrect choice please choose option from the list")
            
    
 