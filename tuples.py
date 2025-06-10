# collection = single "variable" used to store multiple values    
    # Tuple = () ordered and unchangeable. Duplicates OK. FASTER THEN LIST

# example of a tuple
fruits = ("apple", "orange", "banana", "coconut","coconut")

# finding the index of tuple
print(fruits.index("apple"))
print(fruits.count("coconut"))

print()

# tuples are collections so we can iternate on them
for fruit in fruits:
    print(fruit)