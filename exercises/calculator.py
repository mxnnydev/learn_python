# Python Calculator 

# asking for which operator type to use 
operator = input("Enter an operator (+ - * /): ")
# getting first & second digit to operate on 
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))


if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not valid operator")


