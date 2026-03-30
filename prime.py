#wap to check prime number
num =int(input("enter your number "))
for i in range(2,num):
    if num % i ==0:
        print("not prime")
        break
    else:
        print("prime")  