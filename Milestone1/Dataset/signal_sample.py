import numpy as np


def generate_signal(signal_type="sine", amplitude=1, frequency=1, sampling_rate=100, duration=1, save_to_file=None):
    """
    Generates a discrete-time signal and optionally saves it to a file.

    Parameters:
        signal_type (str): Type of the signal ('sine', 'cosine', 'square', 'sawtooth').
        amplitude (float): Amplitude of the signal.
        frequency (float): Frequency of the signal in Hz.
        sampling_rate (int): Sampling rate in Hz.
        duration (float): Duration of the signal in seconds.
        save_to_file (str): File path to save the signal data as a CSV file.

    Returns:
        tuple: A tuple (time, signal) where:
               - time: numpy array of time indices
               - signal: numpy array of signal values
    """
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

    if signal_type == "sine":
        signal = amplitude * np.sin(2 * np.pi * frequency * t)
    elif signal_type == "cosine":
        signal = amplitude * np.cos(2 * np.pi * frequency * t)
    elif signal_type == "square":
        signal = amplitude * np.sign(np.sin(2 * np.pi * frequency * t))
    elif signal_type == "sawtooth":
        signal = amplitude * 2 * (t * frequency - np.floor(t * frequency + 0.5))
    else:
        raise ValueError("Invalid signal_type. Choose from 'sine', 'cosine', 'square', or 'sawtooth'.")

    if save_to_file:
        np.savetxt(save_to_file, signal, delimiter=",")

    return t, signal