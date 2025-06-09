# while loop = execute some code WHILE some condition remains true

# prompt the user for their name
name = input("Enter you name: ")

# while loop runs until name is not empty
while name == "":
    print("You did not enter your name")
    name = input("Please enter your name: ")
# print a greeting message
print(f"Hello {name}!")
