# list are the collection of orderd and mutable data
# lists are written inside the squared brackets seprated by commas
# multiples datatypes can be written inside a list
a=[1,2,3,4,5,6]
a=[1,"apple",12.5,"456"]
print(a)
print(type(a))
for i in a:
    print(i)
#short hand method
[print(i) for i in a]

# slicing
a=['ironman','hulk','captain','thor']
print(a[0])
print(a[:3])
print(a[-2:0]) # empty list
print(a[-2:4])
print(a[::-1])
print(a[2::-1])

#function
a=['ironman','hulk','captain','thor','hulk']
print(len(a))
print(a.count("hulk"))
a.append("spyderman")
print(a)
a.insert(1,'vision')
print(a)
a.remove('hulk')
print(a)
a.pop(1)
print(a)

b=a.copy()
print(b)
b.remove('ironman')
print(b)

print(a.index("hulk"))

b=["satyam","mohit"]
a.extend(b)
print(a)

a.reverse()
print(a)
a.sort()
print(a)

# list compherehnsion
l1=[1,2,3,4,5,6]
l3=[i for i in l1 if i>1]
print(l3)
