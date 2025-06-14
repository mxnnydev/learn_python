# collection = single "variable" used to store multiple values
    # List = [] ordered and changeable. Duplicates OK


# example of a list
fruits = ["apple", "orange", "banana", "coconut"]


print(fruits[0]) # first element
print(fruits[-1]) # last element
print(fruits[::2]) # every second element


# for loop with list
for fruit in fruits:
    print(fruit)


# list of all methods & properties
# print(dir(fruits))

# here a desc of all the methods
# print(help(fruits))

# getting the length of a list
print(len(fruits))

# check if value is in collection
print("apple" in fruits)

# change index 0 value
fruits[0] = "pineapple"

# common methods 
fruits.append("pineapple") # will add the following to the end of the list

fruits.remove("apple") # will remove the apple

fruits.insert(0, "pineapple") # insert pineapple at index 0 

fruits.reverse() # this will reverse the elements (based on the order)

fruits.clear() # to clear a list

index_of_apple = fruits.index("apple") # get the index of the following value

print(index_of_apple) # get the index of apple 

index_non_existent_element = fruits.index("strawberry")

print(index_non_existent_element) # will throw ERROR

print(fruit.count("pineapple")) # return the amount of times it will occur in a list