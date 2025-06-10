# for loops = execute a block of code a fixed number of times.
#             you can iterate over a range, string, sequence, ect

# Example of a basic for loop ~ will count from 1 - 10
print("\nAnother Example ~ simple count\n")

for i in range(1,11):
    print(i)

print("\nAnother Example ~ reversed count\n")

# counting backwards from 10 ~ will start the count from 10 to 1
for i in reversed(range(1,11)):
    print(i)

print("\nAnother Example ~ count in 2's \n")

# counting by 2 now also works 
for i in range(1,11,2):
    print(i) # start at 1 but add 2 to every following number 

print("\nAnother Example ~ count each digit in the credit card\n")

# iterating over a string
credit_card = "1234-5678-9012-3456"

# this will go throught each item in the seqence of strings 
for i in credit_card:
    print(i)