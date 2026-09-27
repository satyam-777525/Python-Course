# functions are the set of code,which one created they can be used throughout the program
def hello():
    print("hello world")

hello()

# parameters and Argument
# parameter-parameter are the variable written inside the parentheses with the name of function.
# Argument-argument are the values passed to the parameters while calling the function.
def sum(x,y):# parameter
    print(x+y)
sum(2,3)#argument
sum(10000,6491654)


def hello(*name):
    print("hello,my name is",name[0])
    print("hello,my name is", name[1])
    print("hello,my name is", name[2])

hello("john","satyam","mohit")  # this is arbitary argument

def h1():
    return "hello"
print(h1)
print(h1())

#recursion
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(6))
