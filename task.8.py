#Aim: WAP to find average of list of numbers entered by the user by single input statement.

num=input("enter numbers you want to find average(seperate number by ,):-")
a=list(map(int,num.split(",")))
print(sum(a)/len(a))



