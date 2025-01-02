#!/usr/bin/env python3
from processor import Processor
import matplotlib.pyplot as plt

class WaveformVisualizer(Processor):
    def __init__(self):
        super().__init__()

    def show(self, t, signals, titles):
        plt.figure(figsize=(12, 6))

        for i, signal in enumerate(signals):
            plt.subplot(len(signals), 1, i + 1)
            plt.plot(t, signal)
            plt.title(titles[i])
            plt.xlabel('t (s)')
            plt.ylabel('amplitude')

        plt.tight_layout()
        plt.show()

WaveformVisualizer().main_visualize(__name__)
