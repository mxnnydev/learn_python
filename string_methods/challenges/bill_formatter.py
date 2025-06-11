# prompt item to buy 
item_buy = input("What do you want to buy: ").strip().capitalize()

# prompt item price 
item_price = float(input("What is the price: "))

# prompt quantity to buy 
item_quantity = int(input("What quantity: "))

# calculate the total
item_cost = item_price * item_quantity

# format bill ~ example format Apple x2 - ₹40.00
print(f"{item_buy} x{item_quantity} - ₹{item_cost:.2f}")


