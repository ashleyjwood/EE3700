import numpy as np
import matplotlib.pyplot as plt

# WORKING WITH ARRAYS AND MATRICES
# Creating Array and Matrices:
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # 3x3 Matrix
B = np.zeros((3, 3))  # 3x3 matrix of zeros
C = np.ones((2, 4))  # 2x4 matrix of ones
D = np.eye(3)  # 3x3 identity matrix

print(f"Matrix A:\n{A}\n")

# Accessing and Modifying Elements:
A[0, 1] = 10  # Modify element at first row, second column
col = A[:, 2]  # Access third column
row = A[1, :]  # Access second row

print(f"Modified Matrix A:\n{A}\n")
print(f"Third column of A:\n{col}\n")
print(f"Second row of A:\n{row}\n")

# Basic Matrix Operations:
A_trans = A.T  # Transpose of A
A_inv = np.linalg.inv(A)  # Inverse of A
A_mult = np.dot(A, B)  # Multiplication of A and B

print(f"Transpose of A:\n{A_trans}\n")
print(f"Inverse of A:\n{A_inv}\n")
print(f"Multiplication of A and B:\n{A_mult}\n")

# Plotting a Sine Wave:
x = np.arange(0, 10, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Wave')
plt.grid(True)
plt.show()
