# moving average filter is a simple yet powerful method used in signal processing to
# smooth out fluctuations (تقلبات) in a signal
#works by averaging a subset of data points (defined by a sliding window)
# and using the average as the new value for the central point.
# as like mean of the signal


import numpy as np
import matplotlib.pyplot as plt

from Milestone1.TASK2_Sampling import sample_signal

from Milestone1.TASK3_Quantization import quantize_signal
# couldn't do for signals in TASK1 MS1 due to missmatch of paths


# from Milestone1.TASK3_Quantization import quantize_signal

# Apply Moving Average Filter (Smoothing)
def moving_average_filter(signal, window_size):
    return np.convolve(signal, np.ones(window_size) / window_size, mode='valid')#max[m,n]-min[m,n]+1
#Return a new array of given shape and type, filled with ones. np.ones() #array of tuple

if __name__ == "__main__":
    # Sampling parameters
    sampling_rate = 200
    duration = 1

    # Get sampled signal from Task 2 of MS1
    sampling_time, sampled_values = sample_signal(sampling_rate, duration)

    # Apply moving average filter with a window size of 10
    window_size = 10
    smoothed_signal = moving_average_filter(sampled_values, window_size)

    # Quantize the smoothed signal
    num_levels = 8  # Example number of quantization levels
    quantized_signal = quantize_signal(smoothed_signal, num_levels)

    # Adjust time axis to match the length of the smoothed signal
    smoothed_time = sampling_time[:len(smoothed_signal)]
    quantized_time = smoothed_time[:len(quantized_signal)]

    # Plot the original and smoothed signals
    plt.figure(figsize=(10, 6))
    plt.plot(sampling_time, sampled_values, label='Original Signal', color='blue', alpha=0.6)
    plt.plot(smoothed_time, smoothed_signal, label='Smoothed Signal (Moving Average)', color='red', alpha=0.8)

    plt.plot(quantized_time, quantized_signal, label='Quantized Signal', color='green', alpha=0.8)
    plt.title('Signal Smoothing and Quantization')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)
    plt.show()
