#wap ofsum of odd and even
num = int(input("enetr your numbers here : "))
i = 1
sum_odd = 0
sum_even = 0
while i<=num:
    if i % 2 == 0:
        sum_even += i
    
    else:
        sum_odd += i
    i +=1
print(sum_even)
print(sum_odd)
