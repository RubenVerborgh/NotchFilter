#!/usr/bin/env python3
from processor import Processor
import numpy as np
import matplotlib.pyplot as plt

class FrequenciesVisualizer(Processor):
    title = "Frequencies"

    def plot(self, axes, t, signal):
        # Transform signal to frequencies
        fft_result = np.fft.fft(signal)
        frequencies = np.fft.fftfreq(len(t), d=self.time_step)

        # Show positive frequencies only
        frequencies = frequencies[:len(t) // 2]
        magnitudes = np.abs(fft_result)[:len(t) // 2]
        magnitudes = magnitudes / max(magnitudes)

        # Draw plot
        plt.plot(frequencies, magnitudes, linewidth=1)
        axes.set_xlabel('frequency (Hz)')
        axes.set_ylabel('magnitude')

FrequenciesVisualizer.main_visualize(__name__)
