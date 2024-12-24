#Quantized Signal=round(sampled values×num_levels)/num_levels
#The difference between the original sampled value and the quantized value is called quantization error.
# sample values = 0.25 and num of levels = 8
# scale 0.25*8 = 2
# rounding to 2 then get scale back by 2/8 = 0.25
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from Milestone1.TASK2_Sampling import sample_signal
# num_levels
# num_levels) determines how finely the amplitude is discretized.
def quantize_signal(sampled_values, num_levels):
    quantized_signal = np.round(sampled_values * num_levels) / num_levels
    return quantized_signal

if __name__ == "__main__":
    # Sampling parameters
    sampling_rate = 200
    duration = 1

    # Get sampled signal from Task 2
    sampling_time, sampled_values = sample_signal(sampling_rate, duration)

# num_levels
# num_levels) determines how finely the amplitude is discretized.
    num_levels = 8
    quantized_signal = quantize_signal(sampled_values, num_levels)

    # Plot the quantized signal
    plt.figure(figsize=(10, 6))
    plt.stem(sampling_time, quantized_signal, linefmt='g-', markerfmt='go', basefmt='g-', label='Quantized Signal')
    plt.title('Quantized Signal')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)
    plt.show()