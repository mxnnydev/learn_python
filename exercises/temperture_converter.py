unit = input("Is this temperature in Celsius or Fahrenheit (C/F) ")
temp = float(input("Enter the temperture: "))

if unit == "C":
    temp = (temp * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {temp}°")
elif unit == "F":
    temp = (temp - 32) * 5/9
    print(f"The temperature in Celsius is: {temp}°")
else:
    print(f"{unit} is an invalid unit of measurement")
