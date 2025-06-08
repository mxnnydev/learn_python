import math

# formula to be used 
# A = pi * radius^2 

# get the radius from the user
radius = float(input("Enter the radius of a circle: "))

# calculate the area
area = math.pi * math.pow(radius,2)

print(f"The area of the circle is: {round(area,2)}cm^2") # display the results
