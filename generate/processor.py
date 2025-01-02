import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

class Processor:
    def __init__(self):
        # Settings
        self.seconds = 1
        self.sample_rate = 44_100
        self.bits = 16

        # Derived properties
        self.samples = int(self.seconds * self.sample_rate)
        self.time_step = 1 / self.sample_rate
        self.bit_depth = 2 ** self.bits
        self.sample_max = (self.bit_depth >> 1) - 1
        self.sample_min = -self.sample_max
        self.nyquist_frequency = self.sample_rate // 2

    def main_generator(self, name):
        if name == '__main__':
            output_file = sys.argv[1]
            signal = self.generate(self.time())
            self.write(signal, output_file)

    def main_filter(self, name):
        if name == '__main__':
            input_file = sys.argv[1]
            output_file = sys.argv[2]

            signal = self.read(input_file)
            filtered = self.filter(signal)

            self.write(filtered, output_file)

    def main_visualize(self, name):
        if name == '__main__':
            files = sys.argv[1:]
            signals = [self.read(f) for f in files]
            self.show(self.time(), signals, files)

    def time(self):
        return np.linspace(0, self.seconds, self.samples, endpoint=False)

    def read(self, file):
        sample_rate, bits = wavfile.read(file)
        # Convert stereo to mono
        if len(bits.shape) > 1:
            bits = bits.mean(axis=1)
        return bits / self.sample_max

    def write(self, signal, file):
        bits = (signal * self.sample_max).astype(np.int16)
        wavfile.write(file, self.sample_rate, bits)

    def normalize(self, signal):
        return signal / np.max(np.abs(signal)) * 0.5

    def generate(self):
        pass

    def filter(self, signal):
        pass

    def show(self, t, signals, titles):
        plt.figure()

        for i, signal in enumerate(signals):
            axes = self.subplot(i + 1, len(signals))
            self.plot(axes, t, signal)
            axes.set_title(titles[i], va='bottom', y=1.2)

        plt.gcf().canvas.manager.set_window_title(self.title)
        plt.tight_layout()
        plt.show()

    def subplot(self, pos, count):
        return plt.subplot(count, 1, pos)

    def plot(self, axes, t, signal):
        pass
