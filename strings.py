#string are the combinations of number ,symobls and letters,enclosed inside quatitons
# string are immutable (not changeable)
from dataclasses import replace

a="satyam"
print(a)
print(type(a))
a="hello"
print(len(a)) # length of string
print(a.count('l')) # count the elemnt
print(a.upper())
print(a.isupper())
print(a.lower())
print(a.islower())
print(a.index('o'))
print(a.index("o",3,5))# if element not found they give error
print(a.capitalize())
print(a.casefold())
print(a.find('e',1,4))#if element not found then return -1
x="my name is {} {}"
print(x.format("satyam","varshney"))
name="john"
print(name.center(10,'x'))# ___john___

# string-2 is functions
a="satyamvarshney77"
print(a.isalnum()) #all are numbers and aplha only
print(a.isalpha()) # all are alphabets
a="123456789"
print(a.isdigit())
a="sdfghjkl788"
print(a.islower())
a=""
print(a.isspace())
a='Satyam'
print(a.istitle())

# string part 3
a="hArry Potter"
print(a.endswith('r'))
print(a.endswith('t',6,9))
print(a.startswith('h'))
print(a.swapcase())

a="   satyam    "
print(a.strip( ))
a="#adg#mjuv#?jfbdjb"
print(a.split("#"))

# ljust() return the left aligment
a="harry potter"
x=a.ljust(20)
print(x,"my favourite movie")
x=a.ljust(20,"#")
print(x,"my favourite movie")

a="harry potter"
x=a.rjust(20,"@")
print(x)


a="my name is john"
print(a.replace("john","satyam"))
a="satyam"
print(a.replace('a','t'))

# rindex() searche the string for a specified value and returns the last position of where it was found
a="laptop is very essential for coding"
print(a.rindex('very'))

a="laptop is very essential for coding"
print(a.rfind("is"))

###################################################################################################################
# slicing in string
a="satyam"
print(a[0])
print(a[0:5])
print(a[-1])
print(a[0:-2])
print(a[3:-2])
print(a[-4:])
print(a[-2:3]) #nothing print()
a="0123456789"
print(a[0:10:2])
print(a[::-1])
print(a[6::-1])


