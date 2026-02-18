#Aim: Write a program to find the two sides of a right angle triangle if hypotenuse and one angle in degrees is given by the user.

import math
print("TWO SIDES OD RIGTH ANGLE IF HYPOTENUSE AND ONE ANGLE IS GIVEN")
hypotenuse=float(input("enter hypotenuse:-"))
angle=float(input("enter angle"))
angle=math.radians(angle)
opposite_side=hypotenuse*math.sin(angle)
ajectant_side=hypotenuse*math.cos(angle)
print(f'''opposite side is {opposite_side}
adjectant side is {ajectant_side}''')