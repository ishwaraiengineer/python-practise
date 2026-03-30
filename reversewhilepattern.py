#wap with pattern loop in reverse
for row in range(6,0,-1):
    for col in range(row):
        print("*",end=" ")
    print()