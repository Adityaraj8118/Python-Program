#Function to add two numbers with user input also we input the value in float.
def add_numbers(num1, num2):
    return num1 + num2
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is {result}")
