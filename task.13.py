#Aim: WAP to find the double factorial of a number.

n=int(input("Enter number:-"))
Double_Factorial=1
for i in range(1,n+1,2):
    Double_Factorial=i*Double_Factorial

print(f"Double Factorial:{Double_Factorial}")