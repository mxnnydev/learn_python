# if = Do some code only IF some condition is True 
#      Else do something else

# get the users age 
age = int(input(f"Enter your age: "))

# conditional control flow
if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print(f"You are now signed up")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sign up")

# another example program

response = input("Would you like food?: (Y/N): ")

if response == 'Y':
    print("Have some food!")
else:
    print("No food for you!")

# another example program

name = input("Enter your name: ")

if name == "":
    print("You did not type in your name")
else:
    print(f"Hello {name}")

# use of Booleans with if statements

for_sale = False

if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale")

# another example like previous one

online = True

if online:
    print("The user is online")
else:
    print("The user is offline")
