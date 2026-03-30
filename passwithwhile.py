#wap for check user id and pass
# WAP for user id and password using while

correct_user = "admin"
correct_pass = "1234"

while True:
    user = input("Enter user id: ")
    password = input("Enter password: ")

    if user == correct_user and password == correct_pass:
        print("Login Successful ")
    