#wap of fibonacci series
num = int(input("enetr your number "))
a=0
b=1
i=1
while i<= num:
    print(a,end=" ")
    c= a+b
    a=b
    b=c
    i += 1
       