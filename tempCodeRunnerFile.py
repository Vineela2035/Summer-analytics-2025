a=int(input())
b=int(input())
list=[1,2,3,5,7,9]
flag=0
if a in list:
    if b in list:
        c=a+b
    else:
        flag=1
else:
    flag=1
if flag==1:
    print("Not available")
else:
    print(c)
if id(a)==id(b):
    print("Same Id's") 
else:
    print("Different Id's")
if a is b :
    print("Both are same")
else:
    print("Both are different")