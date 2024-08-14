import numpy as np
import matplotlib.pyplot as plt

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
f_plot = np.fft.fftfreq(len(fft_signal), period)

plt.plot(f_plot, np.abs(fft_signal))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('FFT of the Signal')
plt.xlim(-25, 25)  # Limit x-axis for better view
plt.grid(True)
plt.show()
