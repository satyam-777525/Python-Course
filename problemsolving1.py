# #swapping
# a=2
# b=3
# temp=a
# a=b
# b=temp
# print("a :",a)
# print("b :",b)
# #convert float into int
# x=12.4
# x=int(x)
# print(x)
# # no. is positive
# a=int(input("enter the number"))
# if(a>=0):
#     print("no. is positive")
# else:
#     print("no. is negative")
# # no. is even or odd
# a=int(input("enter the number"))
# print("no. is even") if(a%2==0) else print("no. is odd")
from itertools import count
from xml.dom.minidom import ProcessingInstruction

#loops problem
# i=1
# sum=0
# while(i<=20):
#     if(i%2!=0):
#         sum=sum+i
#     i=i+1
# print(sum)
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# for i in range(1,5):
#     for j in range(5-i,0,-1):
#         print("*",end=" ")
#     print()
# a=0
# b=1
# print(a)
# print(b)
# for i in range(2,11):
#     c=a+b
#     a=b
#     b=c
#     print(c)

# n=int(input("enter the number"))
# count=0
# # if(n==0):
# #     print("not prime")
# for i in range(1,n+1):
#     if(n%i==0):
#         count+=1
# if(count==2):
#     print("no. is prime")
# else:
#     print("no. is not prime")

# n=int(input("enter the number"))
# rev=0
# a=n
# while(a>0):
#     rev=rev*10+a%10
#     a=a//10
# if(rev==n):
#     print("no. is palindrome")
# else:
#     print("no. is not palindrome")

# a="OOTD.YOLO.ASAP.BRB.GTG.OTW"
# print(a.split('.'))
# print(sorted(a))
# a="hello"
# print(a.replace('e',""))
# z="F.R.E.I.N.D.S"
# print(z.replace(".",""))
# print(z.count('N'))
# a=input("enter the string")
#
# count=0
# for i in range(0,len(a)):
#     if(a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u'):
#         count+=1
# print(count)
# a=["rose","rachel","monica","joe"]
# # temp=a[0]
# # a[0]=a[3]
# # a[3]=temp
# # print(a)
# # a.insert(1,"shiksha")
# # print(a)
# a.pop(2)
# print(a)
# a=[13,7,12,10]
# # m=1
# # for i in a:
# #     m=m*i;
# # print(m)
# l=0
# for i in a:
#     if(i>l):
#         l=i
# print(l)
# print(eval(input("enter the euation :")))

# def maxnum(x,y,z):
#     if(x>y and x>z):
#         return x
#     elif(y>x and y>z):
#         return y
#     else:
#         return z
# print(maxnum(20,25,30))

# def list():
#     a=[]
#     for i in range(1,31):
#         a.append(i**2)
#     return a
# print(list())
# count=0
# def prime(n):
#     count=0
#     for i in range(1,n+1):
#         if(n%i==0):
#             count+=1
#     if(count==2):
#         print("this no. is prime")
#     else:
#         print("this no. is not prime")
# prime(7)
# def sumlist(a):
#     sum=0
#     for i in a:
#         sum=sum+i
#     return sum
# print(sumlist([1,2,3,4,5]))








