#check waether a character is uppar case or case
d = input("Enter a character: ")

if d.isupper():
    print("The character is Uppercase")
elif d.islower():
    print("The character is Lowercase")
else:
    print("The character is not an alphabet")