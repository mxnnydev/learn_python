# validate user input exercise 
    # 1. username is no more than 12 characters 
    # 2. username must not contain spaces
    # 2. username must not contain digits

username = input("Please enter a username: ")

if len(username) <= 12 and username.find(" ") == -1 and username.isalpha():
    print("Username created successfully")