# dictionary = a collection of {key:value} pairs
#               ordered and changeable. No duplicates

# example of dictionary 
capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

# capital keys
capital_keys = capitals.keys()

# capital values
capital_values = capitals.values()




# display all the key values 
print("Keys")
for key in capital_keys:
    print(key)

print() # line break

print("Values")
for value in capital_values:
    print(value)

print(f"\nThe following are key and value pairs using .items()")

# getting both key and value using .items()
for key, value in capitals.items():
    print(f"Country: {key}\nCapital:{value}")
    print()