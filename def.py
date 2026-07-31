# def fun1()
#     print ("hello world")
# fun1()

# def evenodd(x):
#     if x %2== 0:
#         print("even")
#     else:
#         return "odd"
#     [evenodd(16)]
    
# #default
# def greet():
#     print("good morning")

# greet()

# #positional
# def add(a,b):
#     print (a+b)
# add (5,3)

# #keyword arguments

# def student(name,age):
#     print(name,age)
    
# student(name='rahul',age=19)


def fun(arg):
    arg="developer"
    print("id inisde the function: ",id(arg))
    
var="python"
print("before:",id(var))
print("after:",id(var))

# keywords Arguments

# def student(name, age):
#     print(name, age)

# student(age=20, name='Rahul')


# Docstring

# def greeting():
#     '''This is the Docstring of
#     greeting function'''
#     print("hello Good Mornig")
#     return

# greeting()


# def printtime(str):
#     '''This function pass the
#     string into the fuction'''

# def printtime(str):
#     '''This function pass the
#     string into the fuction'''
#     print(str)
#     return
# printtime("hello I am a Print Time Function by user dcefined")

# Refrence value
def fun1(arg):
    arg = "Developer"
    print("Id inside the Function: ", id(arg))

var = "Python"
print("Befor: ", id(var))
fun1(var)
print("After: ", id(var))
