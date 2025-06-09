# get name value from user
name = input("Enter your full name: ")
phone_number = input("Enter your phone #: ")

# length of characters
result = len(name)

# look at some string methods
result = name.find(" ") # Find locates substring's first occurrence.
result = name.rfind(" ") # Find locates substring's last occurrence.

# when using find if nothing is found will return -1

name = name.capitalize() # Will capitalize the first word in a string
name = name.upper() # make everything uppercase
name = name.lower() # make everything lowercase
result = name.isdigit() # will return True or False if string return only digits
result = name.isalpha() # will return True or False if string return only Alphabetical letters
result = phone_number.count("-") # count occurances of certain strings
result = phone_number.replace("-", "") # will replace certain occurances

# display the value
print(result)

# if you need to view all the string method available to you
print(help(str))
