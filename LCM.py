import math
def lcm(x, y, z):
    return abs(x * y * z) // math.gcd(x, y, z)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

lcm_val = lcm(a, b, c)
print(f"The LCM of {a}, {b} and {c} is {lcm_val}")