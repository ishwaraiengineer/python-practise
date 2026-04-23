# updating elements in dict
data = {"name": "khushi", "age": 21}

data["language"] = "python"
data["phone"] = 8476467
data["class"] = 12

print("Updated dict:", data)

# popitem
key, val = data.popitem()
print(f"key: {key}, value: {val}")

# safe delete
if "age" in data:
    del data["age"]

# safe pop
v = data.pop("class", "Key not found")
print("Popped value:", v)

print("Final dict:", data)


# -------- Iteration --------

# iterate keys
for key in data:
    print("Key:", key)

# iterate values
for value in data.values():
    print("Value:", value)

# iterate key-value pairs
for key, val in data.items():
    print(f"key: {key}, value: {val}")