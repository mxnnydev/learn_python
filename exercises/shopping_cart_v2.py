# Shopping cart program

foods = []
prices = []
total = 0 

# will evaluate to True until q is pressed then break
while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q": # if food is Q or q it will break out of while loop 
        break
    else:
        # else if other then Q/q then it will prompt price 
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food) # add the food to the list (foods)
        prices.append(price) # add price to list (prices)

print("----- YOUR CART -----")
for food in foods:
    print(food)

for price in prices:
    total+= price

print()
print(f"Your Total is ${total:.2f}")


