#wap for 3 attempt
user_id = "lucifer"
id_pass = "666666"
attempt = 0
while attempt < 3:
    user = input("enter your user id ")
    password = input("enter your pass ")
    if user == user_id and password == id_pass:
        print("login")
        break
    else:
        print("not login")
        attempt += 1
if attempt ==3:
    print ("id locked")