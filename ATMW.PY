USER_NAME = (input("ENETR YOUR USER NAME = "))
ID_PASS = (input("EMTERB YOUR USER ID PASS = "))
balance = 1000000
pin =7722

if USER_NAME == "lucifer" and ID_PASS == "spideyy_lucky":
    print("access granted")
    
    user_pin = int(input("enetr your pin = "))
    if user_pin == pin:
        print("pin is correct")
        
        amount =int(input("enetr your amount = "))
        if amount<500:
            print("minimum amount of withdrawal amount is 500")
        elif  amount>balance:
            print("insufficient balance")
        else:
            balance-=amount
            print("withdrawal successfull")
            print("your remaining balance", balance)
    else:
        print("pin is incorrect")
        
else:
    print("access invalid")
    

    
