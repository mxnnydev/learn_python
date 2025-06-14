# TypeCasting = the process of converting one data type to another.
                # str(),int(),float(),bool()

name = "Emmanuel"
age = 25
gpa = 3.2
is_student = True

# how to get data type for each variable 
print(type(name)) # results in string data type 
print(type(age)) # results in int data type 
print(type(gpa)) # results in float data type 
print(type(is_student)) # results in boolean data type 

print() # create a line break

# convert values ~ type casting
0
gpa = int(gpa) # convert to int data type 

print(gpa) # 

age = float(age) # convert to float data type

print(age)

age = str(age) # convert to string data type 

print(age)

print(type(age)) # using the type function tell you which data type you will be dealing with

name = bool(name) # convert to boolean data type

print(name)