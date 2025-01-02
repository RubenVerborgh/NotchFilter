#!/usr/bin/env python3
from processor import Processor
import numpy as np
import matplotlib.pyplot as plt

class PolarAverageVisualizer(Processor):
    title = "Polar Average"

    def __init__(self):
        super().__init__()
        self.frequencies = [440, 554.37, 880]

    def subplot(self, pos, count):
        return plt.subplot(1, count, pos, polar=True)

    def plot(self, axes, t, signal):
        for frequency in self.frequencies:
            self.plot_frequency(axes, signal, frequency)
        axes.legend()

    def plot_frequency(self, axes, signal, frequency):
        """Plots an averaged polar plot"""
        # Create bins to storage averages for one revolution
        bin_count = int(self.sample_rate / frequency)
        bins = [[] for _ in range(bin_count)]

        # Spread multiple revolutions across the bins
        t = self.time()
        period = 1 / frequency
        for i in range(len(signal)):
            bin = int(bin_count * (t[i] % period) / period)
            bins[bin].append(signal[i])
        bins = [np.average(bin or [0]) for bin in bins]

        # Create continuous plot
        bins.append(bins[0])
        theta = np.linspace(0, 2 * np.pi, len(bins))
        line, = axes.plot(theta, bins, label=f"{int(frequency)} Hz")
        return line

PolarAverageVisualizer.main_visualize(__name__)
