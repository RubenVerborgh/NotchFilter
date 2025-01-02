#!/usr/bin/env python3
from processor import Processor
import matplotlib.pyplot as plt

class WaveformVisualizer(Processor):
    title = "Waveform"

    def plot(self, axes, t, signal):
        axes.plot(t, signal, linewidth=0.5)
        axes.set_xlabel('t (s)')
        axes.set_ylabel('amplitude')

WaveformVisualizer.main_visualize(__name__)
