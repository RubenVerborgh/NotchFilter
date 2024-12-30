import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import iirnotch, lfilter
from scipy.io.wavfile import wavfile

# Generate a test signal
fs = 44100  # Sampling rate
duration = 5  # seconds
frequencies = [440, 1000, 1500]  # Frequencies to generate
t = np.linspace(0, duration, int(fs * duration), endpoint=False)
signal = sum(np.sin(2 * np.pi * freq * t) for freq in frequencies)
signal = signal / np.max(np.abs(signal)) * 0.5  # Normalize

# Save generated signal to file
default_directory = r'C:\Your\Path\Here'
os.makedirs(default_directory, exist_ok=True)
test_file = os.path.join(default_directory, 'test_notch.wav')
wavfile.write(test_file, fs, (signal * 32767).astype(np.int16))

print(f"Test signal saved to {test_file}")


# Define a notch filter function
def create_notch_filter(freq, Q, fs):
    """Create coefficients for a notch filter."""
    b, a = iirnotch(freq, Q, fs)
    return b, a

def apply_notch_filter(signal, b, a):
    """Apply a notch filter."""
    return lfilter(b, a, signal)

# Choose notch frequency
notch_freq = 1000.0  # Frequency to filter
quality_factor = 30.0  # Quality factor

# Load the generated signal (or any other)
fs, signal = wavfile.read(test_file)
if len(signal.shape) > 1:  # Stereo to mono
    signal = signal.mean(axis=1)

# Create and apply the notch filter
b, a = create_notch_filter(notch_freq, quality_factor, fs)
filtered_signal = apply_notch_filter(signal, b, a)

# Save the filtered signal
filtered_file = os.path.join(default_directory, 'filtered_example.wav')
wavfile.write(filtered_file, fs, filtered_signal.astype(np.int16))

print(f"Filtered signal saved to {filtered_file}")

# Plot original and filtered signal
time = np.arange(len(signal)) / fs

plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(time, signal)
plt.title('Original Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(time, filtered_signal)
plt.title(f'Filtered Signal (Notch at {notch_freq} Hz)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
