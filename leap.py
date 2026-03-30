#w.a.p to check leap year
y = int(input("enter your year:-"))
if (year%4==0 and year % 100 !=00) or (year % 400 ==0):
   print("leap year")
else:
   print("not leap year")