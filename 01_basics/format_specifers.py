# format specifiers = {value:flags} format a value based on what
# flags are inserted
#
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

# variables
price1 = 3.14159
price2 = -987.65
price3 = 12.34

# fixed-point float format specifier example
print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.2f}")

# using format specifers ~ how to add spaces
print(f"Price 1 is ${price1:10}") # allocate spaces
print(f"Price 2 is ${price2:10}") # allocate spaces
print(f"Price 3 is ${price3:10}") # allocate spaces

# combining format specifiers
print(f"Using combine formatter: Price 1 is ${price1:+,.2f}") 
print(f"Using combine formatter: Price 2 is ${price2:+,.2f}") 
print(f"Using combine formatter: Price 3 is ${price3:+,.2f}") 