#!/usr/bin/env python3
from processor import Processor
import numpy as np

class RisingFrequenciesGenerator(Processor):
    def __init__(self):
        super().__init__()
        self.sweep = range(20, 20_000)

    def generate(self, t):
        # Determine frequency and corresponding angle at each step
        freqs = np.linspace(self.sweep.start, self.sweep.stop, len(t))
        angle = 2 * np.pi * freqs * self.time_step

        # Construct signal using phase accumulator
        phase = 0
        signal = np.linspace(0, 0, len(t), endpoint=False)
        for x in range(len(t)):
            signal[x] = np.sin(phase)
            phase = phase + angle[x]

        return self.normalize(signal)

RisingFrequenciesGenerator().main_generator(__name__)
