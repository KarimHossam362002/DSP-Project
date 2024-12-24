import numpy as np
import matplotlib.pyplot as plt
from Milestone2.TASK1_Average_Filter import moving_average_filter
from scipy import signal  # Import scipy.signal as 'signal'

# Noise Reduction Techniques
# 1. Low-pass filter (simple noise reduction technique)
def low_pass_filter(input_signal, cutoff_freq, sampling_rate):
    nyquist = 0.5 * sampling_rate
    normal_cutoff = cutoff_freq / nyquist
    b, a = signal.butter(1, normal_cutoff, btype='low', analog=False)
    return signal.filtfilt(b, a, input_signal)

# 2. Gaussian filter (smoothing) sigma
def gaussian_filter(input_signal, sigma=1):
    return signal.gaussian(len(input_signal), std=sigma)

# 3. Wiener filter (adaptive noise reduction) minimizes the mean square
def wiener_filter(input_signal):
    return signal.wiener(input_signal)

# Noise Reduction for Sampled Signals (after Moving Average)
def plot_sampled_signal_with_noise_reduction():
    # Example noisy sampled signal
    n = np.arange(0, 50, 1)
    sampled_signal = np.sin(2 * np.pi * 5 * n / 50) + np.random.normal(0, 0.2, len(n))  # Original noisy signal

    # Apply Moving Average Filter to smooth the signal
    window_size = 10
    smoothed_signal = moving_average_filter(sampled_signal, window_size)

    # Apply additional noise reduction techniques
    smoothed_signal = low_pass_filter(smoothed_signal, cutoff_freq=5, sampling_rate=50)
    # smoothed_signal = gaussian_filter(smoothed_signal)  # NOT WORKED
    # smoothed_signal = wiener_filter(smoothed_signal)   # NOT WORKED

    # Plot the noisy, smoothed, and noise-reduced signals
    plt.figure(figsize=(10, 6))

    # Plot Noisy Signal
    plt.subplot(3, 1, 1)
    plt.stem(n, sampled_signal, label="Noisy Signal")
    plt.title("Noisy Sampled Signal")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.grid()

    # Plot Smoothed Signal (Moving Average)
    plt.subplot(3, 1, 2)
    plt.stem(n[:len(smoothed_signal)], smoothed_signal, label="Smoothed Signal (Moving Average)")
    plt.title("Smoothed Signal (Moving Average Filter)")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.grid()

    # Plot Noise Reduced Signal
    plt.subplot(3, 1, 3)
    plt.stem(n[:len(smoothed_signal)], smoothed_signal, label="Noise Reduced Signal")
    plt.title("Noise Reduced Signal (After Noise Reduction)")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.grid()

    plt.tight_layout()
    plt.show()

# Example usage:
if __name__ == "__main__":
    plot_sampled_signal_with_noise_reduction()
