# dictionery allows user to write the data in the form of keys and values.
# {},
a={"name":"john","age":12,"gender":"male"}
print(a)
print(type(a))
print(a["name"])

# iteration
a={"name":"john","age":12,"gender":"male"}
for x in a:
    print(x)

for x in a:
    print(a[x])

for x in a.values():
    print(x)
for x in a.items():
    print(x)
# functions
#get
print(a.get("age"))
#item
print(a.items())
#keys
print(a.keys())
#value
print(a.values())
b=a.copy()
print(b)
val = a.pop("name")
print(val)
a.popitem()
print(a)

emp={1:{"name":"satyam","age":20},2:{"name":"mohit","age":22}}
print(emp[1]["age"])

a={"a":12,"b":13,"c":14,"d":15}
print(sorted(a.values()))

a={}
for i in range(1,16):
    a[i]=i**2
print(a)

a={12:"a",56:"b",23:"c",48:"d"}
for i in a:
    b=sorted(a.keys())
print(b)
