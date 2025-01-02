#!/usr/bin/env bash

# Rising frequency
./generate/rising.py output/rising.wav
./filter/notch.py output/rising.wav output/rising_filtered.wav
./visualize/waveform.py output/rising.wav output/rising_filtered.wav &
./visualize/frequencies.py output/rising.wav output/rising_filtered.wav &
./visualize/polar.py output/rising.wav output/rising_filtered.wav &
