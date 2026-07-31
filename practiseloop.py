# Q1: Print numbers from 1 to 10
for i in range(1,11):
    print(i)

# Q2: Print numbers from 20 down to 10 (reverse order)
for i in range(20,9,-1):
    print(i)
    
# Q3: Print multiples of 3 from 3 to 30
for i in range(3,30,3):
    print(i)
    
# Q4: Check and print whether numbers from 0 to 9 are even or odd
for i in range(0,10):
    if i %2==0:
        print("even",i)
    else:
        print("odd",i)

# Q5: Find the sum of numbers from 1 to 100
total = 0
for i in range(1,101):
    total += i
print(total)

# Q6: Find the factorial of 5
total = 1
for i in range(1,6):
    total *= i
print(total)

# Q7: Count and print numbers divisible by 7 between 1 to 50
count = 0
for i in range(1,50):
    if i%7 == 0:
        count+=1
        print(i, "this is multiply by 7")
print("total countable number which is divisible by 7 is ", count)

# Q8: Find the sum of all odd numbers from 1 to 50
sum = 0
for i in range(1,51):
    if i %2 !=0:
        sum += i
print(sum)

# Q9: Print numbers from 1 to 30 and apply FizzBuzz rules
# (Print "Fizz" for multiples of 3, "Buzz" for multiples of 5,
# and "FizzBuzz" for multiples of both 3 and 5)
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", i)
    elif i % 3 == 0:
        print("Fizz", i)
    elif i % 5 == 0:
        print("Buzz", i)
    else:
        print(i) 
        
# Q10: Check whether a number is prime or not
for i in range(2, n):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")