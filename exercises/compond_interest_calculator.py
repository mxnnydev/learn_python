# Python compound interest calculator 
# Uses the following formula: A = P(1 + r/n)^t

# A = final amount
# P = initial principal balance
# r = interest rate 
# t = number of time periods elapsed 

# inital values for each category
principal = 0
rate = 0
time = 0

# getting the principal
while True:
    principal = float(input("Enter the principal amount: "))
    if principal < 0:
        print("Principal can't be less than zero")
    else:
        break

# getting the rate
while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest can't be less than zero")
    else:
        break

# getting the time
while True:
    time = int(input("Enter the interest rate: "))
    if time < 0:
        print("Time can't be less than zero")
    else:
        break

# compound interest calculated
total = principal * pow(1 + rate / 100, time)

# print the results 
print(f"Balance after {time} year/s: ${total:.2f}")