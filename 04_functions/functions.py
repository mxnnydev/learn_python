# functions in Python 

# What is a function?
# Think of a function like a vending machine. You insert something (input), the machine does something inside (logic), and it gives you something back (output).

# declare a function
def introduction():
    print("Lesson on _____ in Python")

# calling a function 
introduction() # this will invoke a function

#  Parameters — Inputs into the function

def introduction(lesson):  # 'lesson' is the input
    print(f"Lesson on {lesson} in Python")

introduction("Functions") # will take the input ~ inject it into the function

# return — What the function gives back
# This sends a value back to where the function was called.

def add(a, b): # this function is used to calculate the sum
    return a + b

sum_value = add(2,2) # will get the sum = 2 + 2 = 4

print(sum_value)

# Main idea of function is that ~ 🔁 Reusable Logic

def square(x):
    return x * x

result_1 = square(4)  # returns 16
result_2 = square(8)  # returns 64



# So, function are just "Vending machines" & Parameters are "Item buttons on machine"

'''
Use Cases:

- Organize code into chunks

- Create tools (mini-programs)

- Reduce repetition

- Build your own Python library

'''