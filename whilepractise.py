# Q1. Print numbers from 1 to 10 using while loop
i = 1
while i <= 10:
    print(i)
    i += 1

print()  # line gap


# Q2. Print numbers from 10 to 1 using while loop
i = 10
while i >= 1:
    print(i)
    i -= 1

print()  # line gap


# Q3. Find the sum of numbers from 1 to 10 using while loop
i = 1
sum = 0
while i <= 10:
    sum += i
    i += 1
print("Sum =", sum)

print()  # line gap


# Q4. Count the number of digits in a given number
num = int(input("Enter your number :- "))
count = 0
while num > 0:
    count += 1
    num = num // 10
print("Digits =", count)



