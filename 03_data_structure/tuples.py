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


# The Following are common set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Intersection (common elements)
common = set1 & set2              # {3, 4}
common = set1.intersection(set2)  # Same thing

# Union (all elements)
all_items = set1 | set2           # {1, 2, 3, 4, 5, 6}
all_items = set1.union(set2)      # Same thing

# Difference (in set1 but not set2)
diff = set1 - set2                # {1, 2}
diff = set1.difference(set2)      # Same thing

# Symmetric difference (in either set, but not both)
sym_diff = set1 ^ set2            # {1, 2, 5, 6}
sym_diff = set1.symmetric_difference(set2)  # Same thing