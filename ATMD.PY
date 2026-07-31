USER_NAME = input("ENTER YOUR USER NAME = ")
ID_PASS = input("ENTER YOUR USER ID PASS = ")
balance = 1000000
pin = 7722

if USER_NAME == "lucifer" and ID_PASS == "spideyy_lucky":
    print("Access Granted")
    
    user_pin = int(input("Enter your PIN = "))
    if user_pin == pin:
        print("PIN is correct")
        
        amount = int(input("Enter deposit amount = "))
        
        if amount <= 0:
            print("Invalid amount")
        else:
            balance += amount
            print("Deposit successful")
            print("Your updated balance =", balance)
            
    else:
        print("PIN is incorrect")
        
else:
    print("Access invalid")