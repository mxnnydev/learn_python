# exercise to teach use case of while loop

age = int(input("Enter your age: "))

while age < 0:
    print("You entered an invalid age.")
    age = int(input("Please enter a valid age: "))

print(f"You are {age} years old!")  # print a message with the age