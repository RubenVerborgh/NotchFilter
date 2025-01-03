import sys
import re
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

class Processor:
    def __init__(self, *options):
        # Settings
        self.seconds = 5
        self.sample_rate = 44_100
        self.bits = 16

        # Derived properties
        self.samples = int(self.seconds * self.sample_rate)
        self.time_step = 1 / self.sample_rate
        self.bit_depth = 2 ** self.bits
        self.sample_max = (self.bit_depth >> 1) - 1
        self.sample_min = -self.sample_max
        self.nyquist_frequency = self.sample_rate // 2

    @classmethod
    def main_generator(cls, name):
        if name == '__main__':
            _, output_file, *options = sys.argv
            generator = cls(*options)

            signal = generator.generate(generator.time())
            generator.write(signal, output_file)

    @classmethod
    def main_filter(cls, name):
        if name == '__main__':
            _, input_file, output_file, *options = sys.argv
            filter = cls(*options)
            signal = filter.read(input_file)

            filtered = filter.filter(signal)
            filter.write(filtered, output_file)

    @classmethod
    def main_visualize(cls, name):
        if name == '__main__':
            files = []
            options = []
            for i, value in enumerate(sys.argv[1:]):
                if options or re.fullmatch(r'^[0-9\.]+$', value):
                    options.append(value)
                else:
                    files.append(value)
            visualizer = cls(*options)
            signals = [visualizer.read(f) for f in files]

            visualizer.show(visualizer.time(), signals, files)

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
