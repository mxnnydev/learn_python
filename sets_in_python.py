# collection = single "variable" used to store multiple values
    # Set = {} unordered and immutable, but Add/Remove OK. NO duplicates

# example of a set
fruits = {"apple", "orange", "banana", "coconut", "coconut"}

print("length of the set is: ", len(fruits)) # get the lenth of set fruits

print("Is the Pineapple inside","pineapple" in fruits ) # checking in certain value is in a set 

print(fruits) # displaying value of a set (the order display is not constant)

# you can't use indexing in set & you can change value of a set but you can remove & add values

fruits.add("pineapple") # this will add pineapple to the set 
fruits.remove("apple") # this will remove apple from the set
fruits.pop() # will remove whatever element is first ~ it is completely random

fruits.clear() # will empty the whole list 
