import random

low = 1
high = 100 
rand_number = random.randint(low,high) # use the randint ~ generate a random number & assign it to the number variable
random_floating_point = random.random() # get a random floating point number 

print(f"Display random number from 1-100\n{rand_number}")
print(f"Display random floating-point number\n{random_floating_point}")

# getting random choice from the sequence
option = ("rock", "paper", "scissors")

# pick option choices at random
random.choice(option) 


# suffle method in python
cards = ["2","3","4","5","6","7","8","9","10","J","Q", "K", "A"]