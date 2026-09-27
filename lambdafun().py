# it is used when an anonymous function is required for a short period of time and it can only have one expression
from operator import ifloordiv

x=lambda b:print(b)
x(4)
a=lambda b,c:b*c
print(a(4,5))

name="satyam"
print(name)
