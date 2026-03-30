#w.a.p to calculate bill in units
units = float(input("enter you unit:-"))

if units <=70:
    bill = units*0
    print("no bill")
elif units <= 100:
    bill = units*5
else:
    bill = units*10
print("total bill is = ",bill)