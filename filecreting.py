# What is File Handling?
# File Handling means working with files (like .txt, .csv) to:
# Store data permanently, Read saved data later, Update or delete content

# Modes:
# "r" = Read file (display error if file not exist)
# "w" = Write file (create file, overwrite old data)
# "a" = Append (add data at end)
# "x" = Create new file (display error if file exists with same name)


# ---------------- WRITE FILE ----------------
file = open("demo2.txt", "w")
file.write("Hello World, I am learning python with data Analytics\n")
file.write("This is File Handling write file Program\n")
file.close()

print("file is created successfully")


# ---------------- READ FILE ----------------
file = open("demo2.txt", "r")
content = file.read()
print("Content:\n", content)
file.close()


# ---------------- APPEND DATA ----------------
file = open("demo2.txt", "a")
file.write("This line is append in file\n")
file.close()


# ---------------- READ FILE AGAIN ----------------
# print("after append in file -----------")

file = open("demo2.txt", "r")
content = file.read()
print("Content:\n", content)
file.close()