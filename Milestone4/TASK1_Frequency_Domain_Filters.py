#The Nyquist frequency defines the maximum frequency that can be represented without distortion(تشويه).

import numpy as np
import matplotlib.pyplot as plt
from Milestone3.TASK1_Convolution import get_convolution_signals
from Milestone3.TASK2_Correlation import get_correlation
from scipy import signal

# Define the filter functions
def low_pass_filter(signal_data, cutoff_freq, sampling_rate):
    nyquist = 0.5 * sampling_rate
    #Nyquist-Shannon sampling theorem, in order to capture all the information in a signal without aliasing
    normal_cutoff = cutoff_freq / nyquist
    b, a = signal.butter(1, normal_cutoff, btype='low', analog=False)
    filtered_signal = signal.filtfilt(b, a, signal_data)
    return filtered_signal

def high_pass_filter(signal_data, cutoff_freq, sampling_rate):
    nyquist = 0.5 * sampling_rate
    # Nyquist-Shannon sampling theorem, in order to capture all the information in a signal without aliasing
    normal_cutoff = cutoff_freq / nyquist
    b, a = signal.butter(1, normal_cutoff, btype='high', analog=False)
    filtered_signal = signal.filtfilt(b, a, signal_data)
    return filtered_signal

def band_pass_filter(signal_data, low_cutoff, high_cutoff, sampling_rate):
    nyquist = 0.5 * sampling_rate
    # Nyquist-Shannon sampling theorem, in order to capture all the information in a signal without aliasing
    low_normal = low_cutoff / nyquist
    high_normal = high_cutoff / nyquist
    b, a = signal.butter(1, [low_normal, high_normal], btype='band', analog=False)
    filtered_signal = signal.filtfilt(b, a, signal_data)
    return filtered_signal

def band_stop_filter(signal_data, low_cutoff, high_cutoff, sampling_rate):
    nyquist = 0.5 * sampling_rate
    # Nyquist-Shannon sampling theorem, in order to capture all the information in a signal without aliasing
    low_normal = low_cutoff / nyquist
    high_normal = high_cutoff / nyquist
    b, a = signal.butter(1, [low_normal, high_normal], btype='bandstop', analog=False)
    filtered_signal = signal.filtfilt(b, a, signal_data)
    return filtered_signal

# Now in MS4, get the results from MS3
def apply_filters():
    # Get the results from MS3 functions
    sampled_signal, smoothed_signal, noise_reduced_signal, convolved_signal = get_convolution_signals()
    sampled_signal, smoothed_signal, noise_reduced_signal, correlation = get_correlation()

    # Define the sampling rate (assumed, adjust as per your data)
    sampling_rate = 50

    # Apply the filters to the convolved signal
    low_passed = low_pass_filter(convolved_signal, cutoff_freq=5, sampling_rate=sampling_rate)
    high_passed = high_pass_filter(convolved_signal, cutoff_freq=5, sampling_rate=sampling_rate)
    band_passed = band_pass_filter(convolved_signal, low_cutoff=3, high_cutoff=8, sampling_rate=sampling_rate)
    band_stopped = band_stop_filter(convolved_signal, low_cutoff=3, high_cutoff=8, sampling_rate=sampling_rate)

    # Plot the original convolved signal and the filtered results
    plt.figure(figsize=(12, 8))

    # Plot Convolved Signal
    plt.subplot(5, 1, 1)
    plt.plot(convolved_signal, label="Convolved Signal")
    plt.title("Original Convolved Signal")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.grid()

    # Plot Low-Passed Signal
    plt.subplot(5, 1, 2)
    plt.plot(low_passed, label="Low-Passed Signal")
    plt.title("Low-Passed Filtered Signal")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.grid()

    # Plot High-Passed Signal
    plt.subplot(5, 1, 3)
    plt.plot(high_passed, label="High-Passed Signal")
    plt.title("High-Passed Filtered Signal")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.grid()

    # Plot Band-Passed Signal
    plt.subplot(5, 1, 4)
    plt.plot(band_passed, label="Band-Passed Signal")
    plt.title("Band-Passed Filtered Signal")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.grid()

    # Plot Band-Stopped Signal
    plt.subplot(5, 1, 5)
    plt.plot(band_stopped, label="Band-Stopped Signal")
    plt.title("Band-Stopped Filtered Signal")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.grid()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    apply_filters()
