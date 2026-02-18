#Aim: WAP to find the greatest of three numbers entered by user.

def greatest(list):
    value1=0
    for i in list:
        if(value1<i):
            value1=i
    return value1

num=input("enter a number:-")
a=list(map(int,num.split(" ")))
print(f"greatest number is {greatest(a)}")
