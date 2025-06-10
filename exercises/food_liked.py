# prompt the user
food = input("What is your favorite food? (q to quit): ")

# run the loop until the user enters 
while food.lower() != 'q':
    print(f"You like {food}!")
    food = input("What is your favorite food? (q to quit): ")

# print message when exiting the while loop 
print("Excited the while loop! Goodbye!")
