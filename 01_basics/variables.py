# variables = A container for a value (string, integer, float, boolean)
#             A variable behaves as if it was the value it contains


# variable (Strings)
first_name = "Emmanuel"
food = "pizza"
email = "bro123@fake.com"


print(first_name)
# use of f-strings allow for injecting values in a string
print(f"Hello my name is {first_name}.")
print(f"You like {food}")
print(f"Yout email is {email}")

print()

# variable (Integers) 
age = 25
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

print()

# variable (Float) 
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"You gpa is: {gpa}")
print(f"You ran {distance}km")

print()

# variable (Boolean) 
is_student = False
for_sale = False
is_online = False

print(f"Are you a student: {is_student}")

if is_online:
    print("You are online")
else:
    print("You are offline")