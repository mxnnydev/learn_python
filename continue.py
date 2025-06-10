# Python Lesson on break & continue 

# continue ~ it will simply skip the code below 
# break ~ it will halt the code and end the while loop 

# this is a example of ~ continue  
for x in range(1,21):
    if x == 13:
        continue # when this condition is true run this and skips the code below
    else:
        print(x) # print number to terminal

# this is a example of ~ break
for x in range(1,21):
    if x == 13:
        break # when this condition is true runs this and breaks out of the while loop
    else:
        print(x) # print number to terminal