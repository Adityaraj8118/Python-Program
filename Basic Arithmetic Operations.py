a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

sum_val = a + b
Sub_val = a - b
product_val = a * b
quotient_val = a / b if b != 0 else 'Undefined (division by zero)'
remainder_val = a % b

print(f"Sum: {sum_val}")
print(f"Difference: {Sub_val}")
print(f"Product: {product_val}")
print(f"Quotient: {quotient_val}")
print(f"Remainder: {remainder_val}")