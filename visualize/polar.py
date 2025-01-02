#!/usr/bin/env python3
from processor import Processor
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

class PolarVisualizer(Processor):
    title = "Polar"

    def __init__(self):
        super().__init__()
        self.frequencies = [440, 880]

    def subplot(self, pos, count):
        return plt.subplot(1, count, pos, polar=True)

    def plot(self, axes, t, signal):
        lines = [
            self.plot_frequency(axes, signal, frequency)
            for frequency in self.frequencies
        ]
        handles = [
            Line2D([0], [0], color=line.get_color(), lw=2, label=line.get_label())
            for line in lines
        ]
        axes.legend(handles=handles)

    def plot_frequency(self, axes, signal, frequency):
        t = np.linspace(0, frequency * self.seconds, len(signal))
        theta = 2 * np.pi * t
        line, = axes.plot(theta, signal, linewidth=0.1, label=f"{int(frequency)} Hz")
        return line

PolarVisualizer().main_visualize(__name__)
