#Aim: Write a program to Read two numbers and swap them without using a third variable.

num1=int(input("enter first number:-"))
num2=int(input("enter second number:-"))
print(f"before swaping:num1={num1},num2={num2}")
num1,num2=num2,num1
print(f"after swaping:num1={num1},num2={num2}")