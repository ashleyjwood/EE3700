import numpy as np
import matplotlib.pyplot as plt

# GENERATING AWGN NOISES
# Generating AWGN with nominal power:
NUMBER_OF_SAMPLES = 100
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
