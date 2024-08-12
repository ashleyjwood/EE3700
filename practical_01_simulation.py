import numpy as np
import matplotlib.pyplot as plt

NUMBER_OF_SAMPLES = 101

transmitted_signal = np.random.randn(NUMBER_OF_SAMPLES)
for i in range(NUMBER_OF_SAMPLES):
    transmitted_signal[i] = 1 if transmitted_signal[i] > 0 else -1
print(f"Noise:\n{transmitted_signal[:10]}...\n")  # Sample of transmitted signal

signal_power = np.var(transmitted_signal)

print(f"Signal Power:\n{signal_power}\n")

# SNR values in dB to simulate
snr_db_values = [-5, 0, 5, 10, 15]  # Signal to Noise Ratio (SNR)

# Simulation
error_rates = []

for snr in snr_db_values:
    snr_linear = 10 ** (snr / 10)
    noise_power = signal_power / snr_linear
    noise = np.sqrt(noise_power) * np.random.randn(NUMBER_OF_SAMPLES)
    received_signal = transmitted_signal + noise
    detected_signal = (received_signal > 0).astype(int)
    detected_signal[detected_signal == 0] = -1

    error_rate = sum(detected_signal != transmitted_signal) / NUMBER_OF_SAMPLES
    error_rates.append(error_rate)
    print(f"SNR (dB): {snr:>2}, Error Rate: {error_rate:.4f}")

    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(noise)
    plt.plot(transmitted_signal)
    plt.title(f'Transmitted and Noise Signals (SNR = {snr} dB)')
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    plt.grid(True, which="both", ls="--")

    plt.subplot(2, 1, 2)
    plt.plot(received_signal)
    plt.title('Received Signal with Noise')
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.grid(True, which="both", ls="--")
    plt.show()

# Plot Error Rate vs. SNR
plt.figure(figsize=(10, 6))
plt.plot(snr_db_values, error_rates, marker='o')
plt.title('Error Rate vs. SNR')
plt.xlabel('SNR (dB)')

plt.ylabel('Error Rate')
plt.yscale('log')  # Set y-axis to log scale
plt.grid(True, which="both", ls="--")
plt.show()
