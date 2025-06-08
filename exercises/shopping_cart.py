# Exercise 2 Shopping Cart Program 

item = input("What item would you like to buy?: ")
price = float(input("what is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"you have brought {quantity} x {item}/s")
print(f"Your total is: ${total}")
j