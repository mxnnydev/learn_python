# importing math module
import math 

# formula for getting circumference of the circle is 
# C = 2 * pi * radius

# getting the radius from the user 
radius = float(input("Enter the radius of a circle: "))

# calculate the circumference
circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference,2)}cm")