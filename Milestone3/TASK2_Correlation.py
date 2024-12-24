import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from Milestone2.TASK1_Average_Filter import moving_average_filter
from Milestone2.TASK2_Noise_Reduction import low_pass_filter

def get_correlation():
    # Example noisy sampled signal (after noise)
    n = np.arange(0, 50, 1)
    sampled_signal = np.sin(2 * np.pi * 5 * n / 50) + np.random.normal(0, 0.2, len(n))  # Original noisy signal

    # Apply Moving Average Filter to smooth the signal
    window_size = 10
    smoothed_signal = moving_average_filter(sampled_signal, window_size)

    # Apply Noise Reduction (Low-pass filter)
    noise_reduced_signal = low_pass_filter(smoothed_signal, cutoff_freq=5, sampling_rate=50)

    # Calculate Correlation between the Moving Average Filtered and Noise Reduced Signal
    correlation = np.correlate(smoothed_signal, noise_reduced_signal, mode='full')  # Full correlation

    return sampled_signal, smoothed_signal, noise_reduced_signal, correlation

# Call this function in MS4 to get the correlation







# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import signal
# from Milestone2.TASK1_Average_Filter import moving_average_filter
# from Milestone2.TASK2_Noise_Reduction import low_pass_filter
#
# # Correlation Calculation function
# def calculate_correlation(signal1, signal2):
#     correlation = np.correlate(signal1, signal2, mode='full')  # Full correlation
#     return correlation
#
# # Plotting function to show correlation between the signals
# def plot_correlation():
#     # Example noisy sampled signal (after noise)
#     n = np.arange(0, 50, 1)
#     # 0..1..2..48.49 step 1
#     sampled_signal = np.sin(2 * np.pi * 5 * n / 50) + np.random.normal(0, 0.2, len(n))  # Original noisy signal
#
#     # Apply Moving Average Filter to smooth the signal
#     window_size = 10
#     smoothed_signal = moving_average_filter(sampled_signal, window_size)
#
#     # Apply Noise Reduction (Low-pass filter)
#     noise_reduced_signal = low_pass_filter(smoothed_signal, cutoff_freq=5, sampling_rate=50)
#
#     # Calculate Correlation between the Moving Average Filtered and Noise Reduced Signal
#     correlation = calculate_correlation(smoothed_signal, noise_reduced_signal)
#
#     # Generate a time axis for the correlation plot
#     n_corr = np.arange(-len(smoothed_signal) + 1, len(smoothed_signal))
#
#     # Plot the original, smoothed, noise-reduced, and correlation signals
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
#     # Plot Correlation between Moving Average and Noise Reduced Signals
#     plt.subplot(4, 1, 4)
#     plt.plot(n_corr, correlation, label="Correlation between Signals")
#     plt.title("Correlation between Smoothed and Noise Reduced Signals")
#     plt.xlabel("Lag")
#     plt.ylabel("Correlation")
#     plt.grid()
#
#     plt.tight_layout()
#     plt.show()
#
# # Example usage:
# if __name__ == "__main__":
#     plot_correlation()
