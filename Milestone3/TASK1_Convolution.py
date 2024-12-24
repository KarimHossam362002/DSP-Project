import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from Milestone2.TASK1_Average_Filter import moving_average_filter
from Milestone2.TASK2_Noise_Reduction import low_pass_filter

def get_convolution_signals():
    # Example noisy sampled signal (after noise)
    n = np.arange(0, 50, 1)
    sampled_signal = np.sin(2 * np.pi * 5 * n / 50) + np.random.normal(0, 0.2, len(n))  # Original noisy signal

    # Apply Moving Average Filter to smooth the signal
    window_size = 10
    smoothed_signal = moving_average_filter(sampled_signal, window_size)

    # Apply Noise Reduction (Low-pass filter)
    # Other filters not working :(
    noise_reduced_signal = low_pass_filter(smoothed_signal, cutoff_freq=5, sampling_rate=50)

    # Perform Convolution between the smoothed and noise-reduced signals
    convolved_signal = np.convolve(smoothed_signal, noise_reduced_signal, mode='same')  # 'same' keeps the same size

    return sampled_signal, smoothed_signal, noise_reduced_signal, convolved_signal

























# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import signal
# from Milestone2.TASK1_Average_Filter import moving_average_filter
# from Milestone2.TASK2_Noise_Reduction import low_pass_filter
#
# # Convolution of two signals (after Moving Average and Noise Reduction)
# def plot_convolution():
#     # Example noisy sampled signal (after noise)
#     n = np.arange(0, 50, 1)
#     #0..1..2..48.49 step 1
#     sampled_signal = np.sin(2 * np.pi * 5 * n / 50) + np.random.normal(0, 0.2, len(n))  # Original noisy signal
#
#     # Apply Moving Average Filter to smooth the signal
#     window_size = 10
#     smoothed_signal = moving_average_filter(sampled_signal, window_size)
#
#     # Apply Noise Reduction (Low-pass filter, you can change to other methods like Wiener or Gaussian)
#     noise_reduced_signal = low_pass_filter(smoothed_signal, cutoff_freq=5, sampling_rate=50)
#
#     # Perform Convolution between the smoothed and noise-reduced signals
#     convolved_signal = np.convolve(smoothed_signal, noise_reduced_signal, mode='same')  # 'same' keeps the same size
#
#     # Plot the original, smoothed, noise-reduced, and convolved signals
#     plt.figure(figsize=(12, 8))
#
#     # Plot Noisy Signal
#     plt.subplot(4, 1, 1)
#     plt.stem(n, sampled_signal, label="Noisy Signal")
#     plt.title("Original Noisy Signal")
#     plt.xlabel("Samples")
#     plt.ylabel("Amplitude")
#     plt.grid()
#
#     # Plot Smoothed Signal (Moving Average)
#     plt.subplot(4, 1, 2)
#     plt.stem(n[:len(smoothed_signal)], smoothed_signal, label="Smoothed Signal (Moving Average)")
#     plt.title("Smoothed Signal (Moving Average Filter)")
#     plt.xlabel("Samples")
#     plt.ylabel("Amplitude")
#     plt.grid()
#
#     # Plot Noise Reduced Signal
#     plt.subplot(4, 1, 3)
#     plt.stem(n[:len(noise_reduced_signal)], noise_reduced_signal, label="Noise Reduced Signal (Low-pass Filter)")
#     plt.title("Noise Reduced Signal (Low-pass Filter)")
#     plt.xlabel("Samples")
#     plt.ylabel("Amplitude")
#     plt.grid()
#
#     # Plot Convolved Signal
#     plt.subplot(4, 1, 4)
#     plt.stem(n[:len(convolved_signal)], convolved_signal, label="Convolved Signal (Smoothed * Noise Reduced)")
#     plt.title("Convolution of Smoothed and Noise Reduced Signals")
#     plt.xlabel("Samples")
#     plt.ylabel("Amplitude")
#     plt.grid()
#
#     plt.tight_layout()
#     plt.show()
#
# # Example usage:
# if __name__ == "__main__":
#     plot_convolution()
