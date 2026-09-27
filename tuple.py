# tuple are the collection of ordered and im-mutable data
# use paranthesis and multiple data types inside a tuple
a=(1,2,3,5,9,"john")
print(a)
print(type(a))
# if one element in a tuple this is a string if solve this problem use a comma
a=("krishna",)
print(type(a))

# slicing is same as list and string
#######################################################
# conversion of tuples and tuple function
# converstion is very useful because tuples are immutable they are convert into list and change them
a=("vivo","oneplus","samsung","nokia")
print(type(a))
a=list(a)
print(type(a))
a[1]="redmi"
print(a)
a=tuple(a)
print(a)

# function

print(a.count("redmi"))
print(a.index("vivo"))