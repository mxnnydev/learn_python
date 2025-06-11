# Rounding a floating-point number to 2 decimal places

def round_two_decimal(floating_point_number): return f"{round(floating_point_number, 2):.2f}"

# Test values
print(round_two_decimal(5.6789))   # 5.68
print(round_two_decimal(3.14159))  # 3.14
print(round_two_decimal(9.999))    # 10.00