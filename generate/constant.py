#!/usr/bin/env python3
from processor import Processor
import numpy as np

class ConstantFrequenciesGenerator(Processor):
    def __init__(self):
        super().__init__()
        self.frequencies = [440, 1000, 1500]

    def generate(self, t):
        signal = sum(np.sin(2 * np.pi * freq * t) for freq in self.frequencies)
        return self.normalize(signal)

ConstantFrequenciesGenerator().main_generator(__name__)