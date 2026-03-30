#count number with while
f = int(input("enter your number"))
count = 0
while f>0:
    count += 1
    f%= 10
print(count)
    