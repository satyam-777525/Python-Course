age=18
if(age>=18):
    print("you are eligible")
else:
    print("you are not eligible")

# if elif else
marks=98
if(marks>=90 and marks<=100):
    print("you are topper student")
elif(marks>=80):
    print("you are a good student")
else:
    print("you are a student")

# nested if - if ke andr if
hobby="cricket"
age=18
if(age>=18):
    if(hobby =="cricket"):
        print("yes! you are eligible")
    else:
        print("oops! something wrong")

# shorthand if
n=5
if(n==5):print("yes")
# shorthand if else
gen="male"
print("you are a boy") if(gen=="male") else print("you are a girl")


