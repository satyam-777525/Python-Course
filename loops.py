from errno import ELOOP

sum=0
for i in range(0,10):
    sum=sum+i
print(sum)

a=7
for i in range(1,11):
    print(a,"x",i,"=",a*i)

n=777
while(n>0):
    print(n)
    n=n//10
# while true
# it is an infinite  LOOP to break a loop use a break statement
while True:
    print("satyam")
    break;
for i in range(1, 5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(1,10):
    if(i==5):
        print("this mine")
    else:
        print("oo")
# break and continue
for i in range(1,10):
    if(i==2):
        continue
    elif(i==6):
        break
    else:
        print(i)


