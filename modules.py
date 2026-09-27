#modules are the (.py) files,that contain set of functions you want to include in your program
# datetime random math
import datetime
x=datetime.datetime.now()
print(x)
y=datetime.datetime(1977,10,14)
print(y)
print(y.strftime("%A"))
print(y.strftime("%a"))
print(y.strftime("%B"))
print(y.strftime("%m"))
print(y.strftime("%Y"))
print(y.strftime("%y"))
print(y.strftime("%p"))

import random
print(random.randint(1,10))
l=["heads","tails"]
print(random.choice(l))

import math
print(max(13,85,96))
print(pow(2,6))
print(math.sqrt(64))
print(abs(-15))
print(math.ceil(2.3))
print(math.floor(2.99))


import demo # demo.py
a=demo.add(2,3)
print(a)

x=demo.a[0]
print(x)