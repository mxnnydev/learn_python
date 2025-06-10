# Number game 

# prompt get the user number input
num = int(input("Enter a # between 1 - 10: "))

# run while loop if the number is not valid
while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))

# if valid print the following message
print(f"Your number is {num}")