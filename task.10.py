#Aim: WAP to find if a string entered by user is a palindrome or not.

def palindrome_checker(a):
    b=a[::-1]
    if(a==b):
        return True
    else:
        return False

string=input("enter a string:-")
if(palindrome_checker(string)==True):
    print("string is a palindrome")
else:
    print("string is not a palindrome")