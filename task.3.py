#Aim:Write a program to find Hypotenuse of a triangle given its two sides. Use the Pythagoras theorem.

print("PROGRAM TO CALULATE HYPOTENUSE OF TRIANGLE ")
side1=int(input("Enter side 1 of the triangle:-"))
side2=int(input("Enter side 2 of the triangle:-"))
hypothenuse=(side1**2+side2**2)**(1/2)
print(f"hypothenuse of triangle is {hypothenuse}")