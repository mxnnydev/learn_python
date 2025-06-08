import math

# formula 
# C = sqrt(a^2 + b^2)

# getting the following data from the user
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f"Side C = {c}")