# dictionary = a collection of {key:value} pairs
#               ordered and changeable. No duplicates

# example of dictionary 
capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}


# getting value from dictionary 
print(capitals.get("India")) # will return the value associated with the key India

print(capitals.get("Japan")) # Does not exist ~ return None

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exists")

capitals.update({"Germany": "Berlin"}) # allow us to add/update previous key values
capitals.update({"USA": "Detroit"})

capitals.pop("China") # remove key-value pairs
capitals.popitem() # will remove the latest added key value pair 


# get only key of object
keys = capitals.keys()
print(f"The following are keys of capital\n{keys}")

for key in capitals.keys():
    print(key)

# get only value of object
values = capitals.values()
print(f"The following are values of capital\n{values}")

for value in capitals.values():
    print(value)

# using items() in objects 
items = capitals.items()

for key, value in capitals.items():
    print(f"Country 👉 {key} Capital 👉 {value}")