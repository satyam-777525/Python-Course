#conversion of one data type to another is called typecasting
# there are two type
# 1.implicit-python itself changes
# 2.explicit-where users converts one datatype to another

a=123
b=12.3
print(type(a))
print(type(b))

print(type(a+b))#implicit
a="123"
a=int(a)#explicit
b=1
print(type(a+b))