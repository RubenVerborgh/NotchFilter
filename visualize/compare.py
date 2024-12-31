#!/usr/bin/env python3
from processor import Processor
import matplotlib.pyplot as plt

class CompareGraphs(Processor):
    def __init__(self):
        super().__init__()

    def show(self, t, signals):
        plt.figure(figsize=(12, 6))
        plt.subplot(2, 1, 1)
        plt.plot(t, signals[0])
        plt.title('Original Signal')
        plt.xlabel('t [s]')
        plt.ylabel('Amplitude')

        plt.subplot(2, 1, 2)
        plt.plot(t, signals[1])
        plt.title(f'Filtered Signal')
        plt.xlabel('t [s]')
        plt.ylabel('Amplitude')

        plt.tight_layout()
        plt.show()

CompareGraphs().main_visualize(__name__)
