# nested loop = A loop within another loop (outer, inner)
#              outer loop:
#              inner loop:

# nested loop
# for x in range(3):
#     for y in range(1,10):
#         print(y, end="")
#     print()

# rectangle shape 
row  = int(input("Enter the # of rows: "))
columns  = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(row):
    for y in range(columns):
        print(symbol, end="")
    print()
