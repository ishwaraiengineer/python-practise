# Create a dictionary using two lists

keys = ["a", "b", "c", "d"]
values = [10, 20, 30, 40]

my_dict = {}

for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

print(my_dict)   