import numpy as np

n = int(input("Enter number of students: "))

marks = []

for i in range(n):
    mark = int(input(f"Enter marks {i+1}: "))
    marks.append(mark)
 
arr = np.array(marks)

print("\nMarks List:", arr)
print("Maximum Marks:", np.max(arr))
print("Minimum Marks:", np.min(arr))
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))