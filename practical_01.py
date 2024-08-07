import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Matrix
B = np.zeros((3, 3))  # 3x3 matrix of zeros
C = np.ones((2, 4))  # 2x4 matrix of ones
D = np.eye(3)  # 3x3 identity matrix
# print(D)

print(f"{A}\n")
A[0, 1] = 10  # Modify element
col = A[:, 2]  # Access third column
row = A[1, :]  # Access second row

print(f"{A}\n")
print(col)
print(row)


A_trans = A.T  # Transpose
A_inv = np.linalg.inv(A)  # Inverse
A_mult = np.dot(A, B)  # Multiplication
# print(A_mult)

x = np.arange(0, 10, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Wave')
plt.show()
