# 2D List ~ they are just list made of list 

# examples of 2D lists
groceries = [
    ["apple", "orange", "banana", "coconut"],
    ["celery", "carrots", "potatoes"],
    ["chicken", "fish", "turkey"]]

# how to access values from a 2D lists
groceries[0][0]

# iterating on a 2D list

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

