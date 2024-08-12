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

# SIGNAL GENERATION AND BASIC ANALYSIS
# Generating signals:
t = np.arange(0, 1, 0.01)
signal = np.sin(2 * np.pi * 10 * t)

frequency = 100  # Sampling frequency
period = 1 / frequency
n = np.arange(0, 1, period)
sampled_signal = np.sin(2 * np.pi * 10 * n)

# FFT and Frequency Domain Plot
fft_signal = np.fft.fft(signal)
f = np.fft.fftfreq(len(fft_signal), period)

plt.plot(f, np.abs(fft_signal))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('FFT of the Signal')
plt.xlim(-25, 25)  # Limit x-axis for better view
plt.grid(True)
plt.show()

# GENERATING AWGN NOISES
# Generating AWGN with nominal power:
NUMBER_OF_SAMPLES = 1000
noise = np.random.randn(NUMBER_OF_SAMPLES)

# Generating AWGN with specified power:
SPECIFIED_POWER = 0.5  # Can be any number
noise_power = np.var(noise)  # Compute the current power
scaling_factor = np.sqrt(SPECIFIED_POWER / noise_power)
scaled_noise = noise * scaling_factor

# Visualising the noise:
plt.figure()

plt.subplot(2, 1, 1)
plt.plot(noise)
plt.title('AWGN with Nominal Power')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(scaled_noise)
plt.title('AWGN with Specified Power')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
