import numpy as np
import matplotlib.pyplot as plt
# Define the continuous signal

def sample_signal(sampling_rate, duration):
    def continuous_signal(t):
        return np.sin(2 * np.pi * 5 * t)  # 5 Hz sine wave

    continuous_time = np.linspace(0, duration, 1000)  # High-resolution time axis
    continuous_values = continuous_signal(continuous_time)

    sampling_time = np.arange(0, duration, 1 / sampling_rate)  # Sampled time points #samping rate->Fs
    sampled_values = continuous_signal(sampling_time)

    # Plot the signals
    plt.figure(figsize=(10, 6))
    plt.plot(continuous_time, continuous_values, label='Continuous Signal', color='blue', alpha=0.6)
    plt.stem(sampling_time, sampled_values, linefmt='r-', markerfmt='ro', basefmt='r-', label='Sampled Signal')
    plt.title('Continuous Signal and Sampled Signal')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)
    plt.show()

    return sampling_time, sampled_values

if __name__ == "__main__":
    sampling_rate = 200
    duration = 1
    sample_signal(sampling_rate, duration)