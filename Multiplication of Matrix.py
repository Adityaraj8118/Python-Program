import numpy as np

# Define matrix A
A = np.array([[1, 2], [3, 4]])

# Define matrix B
B = np.array([[5, 6], [7, 8]])

# Multiply matrices A and B
C = np.dot(A, B)

print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
print("Result of A * B:")
print(C)