#!/usr/bin/env python3
from processor import Processor
from scipy.signal import iirnotch, lfilter

class NotchFilter(Processor):
    def __init__(self):
        super().__init__()
        self.notch_freq = 1000.0
        self.quality_factor = 30.0

    def filter(self, signal):
        # Define a notch filter function
        def create_notch_filter(freq, Q):
            """Create coefficients for a notch filter."""
            b, a = iirnotch(freq, Q, self.sample_rate)
            return b, a

        def apply_notch_filter(signal, b, a):
            """Apply a notch filter."""
            return lfilter(b, a, signal)

        # Create and apply the notch filter
        b, a = create_notch_filter(self.notch_freq, self.quality_factor)
        filtered = apply_notch_filter(signal, b, a)

        return filtered

NotchFilter().main_filter(__name__)
