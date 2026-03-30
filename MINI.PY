# MINI ATM

BALANCE = 7800

receiver = float(input("Enter withdrawal amount: "))

if receiver <= BALANCE:
    amt = BALANCE - receiver
    print("Remaining Balance:", amt)
else:
    print("Insufficient Balance!")