# sets are unordered collection of data.(elemnt not have proper indexing) this is mutable
#this is unique amd separetd by commas
a={"Ironman","hulk","thor","captain"}
print(a)
print(type(a))
for x in a:
    print(x)

# functions
a.add("vision")
print(a)
a.pop()
print(a)
a.remove("thor")
print(a)
b=a.copy()
print(b)


# important functions
a={"ironman","hulk","thor","captain america"}
b={"superman","batman","wonder"}
c={"hulk","thor","superman"}
#isdisjoint
print(a.isdisjoint(b)) # common h kuch
print(a.isdisjoint(c))
#issubset
print(c.issubset(a))
#issuperset
print(a.issuperset(c))
#update
a.update(c) # common ko hta dega
print(a)

#functions
a={"ironman","hulk","thor","captain america"}
b={"superman","batman","wonder"}
c={"hulk","thor","superman"}
print(a.union(c))
print(a.difference(c)) #a-c (ye sirf btat h konse differences h
a.difference_update(c) # a ko hi update kr dena
print(a)
x=a.intersection(c)
print(x)