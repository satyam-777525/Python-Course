# local variable- are restricted to only one block of code and cannot be changed throughout the program.
# global variable- are not restricted to one block of code and changed throughout the program.
# local
x=15
print("before call",x)
def hello():
    x=20
    return x
print(hello())
print("after call",x)

#global

a=15
print("before call",a)
def hello1():
     global a
     a=20
     return a

print(hello1())
print("after call",a)
