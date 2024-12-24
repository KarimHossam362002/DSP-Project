import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


# 1 Function to plot continuous and discrete sine waves
def plot_sinusoidal():
    t = np.linspace(0, 1, 500)  # Continuous time vector \ linear continuous space
    n = np.arange(0, 50, 1)  # Discrete time vector \ range from 0 to 50
    continuous_signal = np.sin(2 * np.pi * 5 * t)
    discrete_signal = np.sin(2 * np.pi * 5 * n / 50)

    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(t, continuous_signal, label="Continuous Sinusoidal")
    plt.title("Continuous Sinusoidal Signal")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.stem(n, discrete_signal, label="Discrete Sinusoidal")
    plt.title("Discrete Sinusoidal Signal")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.tight_layout()
    plt.show()


# 2 Function to plot continuous and discrete square waves
def plot_square_wave():
    t = np.linspace(0, 1, 500)  # Continuous time vector
    n = np.arange(0, 50, 1)  # Discrete time vector

    continuous_signal = signal.square(2 * np.pi * 5 * t)
    discrete_signal = signal.square(2 * np.pi * 5 * n / 50)

    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.plot(t, continuous_signal, label="Continuous Square Wave")
    plt.title("Continuous Square Wave Signal")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.stem(n, discrete_signal, label="Discrete Square Wave")
    plt.title("Discrete Square Wave Signal")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.grid()

    plt.tight_layout()
    plt.show()


# 3 Function to plot a signal mn file
def plot_from_file(file_path="Dataset/mitbih_test.csv"):
    data = np.loadtxt(file_path, delimiter=",")
    plt.figure(figsize=(10, 4))
    plt.plot(data, label="Signal from file mitbih_test")
    plt.title("Signal from File")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.tight_layout()
    plt.show()


# 4 Function to plot a signal from equation
def plot_from_equation(equation, time_range):
    t = np.linspace(time_range[0], time_range[1], 500)
    input_signal = eval(equation)

    plt.figure(figsize=(10, 4))
    plt.plot(t, input_signal, label=f"Signal: {equation}")
    plt.title(f"Signal from Equation: {equation}")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.tight_layout()


plt.show()
# Example usage:
if __name__ == "__main__":

    # Plot sinusoidal signals
    plot_sinusoidal()

    # Plot square wave signals
    plot_square_wave()

    # Plot signal from a given equation (e.g., sinusoidal equation)
    # plot_from_equation("np.sin(2 * np.pi * 5 * t)", (0, 1))  # Example equation

    # Plot signal from file (file should contain a single column of numeric data)
    plot_from_file("Dataset/mitbih_test.csv")  # Uncomment and provide the file path
