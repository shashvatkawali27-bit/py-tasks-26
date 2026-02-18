#Aim: WAP to read a comma seperated string of numbers as input and generate a new list with even indexes squared and odd indexes cubed.

n=list(map(int,input("Enter string of numbers:").split(",")))
result=[n[i]**2 if i%2==0 else n[i]**3 for i in range(0,len(n))]
print(result)
