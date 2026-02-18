#Aim: Write a program to find the solutions to a quadratic equation
#ax^2 + bx + c = 0. Take a, b, c from User. Assume only real solutions.

print("SOLUTION OF A QUADRIC EQUATION")
print("enter a,b,c in ax^2+bx+c=0")
a=int(input("enter a:-"))
b=int(input("enter b:-"))
c=int(input("enter c:-"))
print(f"the quadric equation is {a}x^2+{b}x+{c}=0")
delta=b**2-4*a*c
if(delta<0):
    print("do not have solution")
  
else:
    x1=(-b+(delta)**(1/2))/2*a
    x2=(-b-(delta)**(1/2))/2*a
    print(f"the solution of quadric equation is {x1},{x2}")
