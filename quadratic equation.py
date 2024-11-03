# Solve ax^2 + bx + c = 0
import cmath
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    return root1, root2
a = 1
b = -7
c = 12
roots = solve_quadratic(a, b, c)
print(f"The roots of the quadratic equation are: {roots[0]} and {roots[1]}")