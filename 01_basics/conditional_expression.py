# conditional expression = A one-line shortcut for the if-else statement (ternary operation)
                           # Print or assign one of two values based on a condition
                           # X if condition else Y

num = 5
a = 6 
b = 7 
age = 25
temperature = 20
user_role = "guess"
# print("Positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b # get the maximum number
min_num = a if a < b else b # get the minimum number
status = "Adult" if age >= 18 else "Child" # based on given age assign some value
weather = "HOT" if temperature > 20 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(access_level) 

# display the results
print(f"The Maximum number is {max_num}\nThe Minimum number is {min_num}")
