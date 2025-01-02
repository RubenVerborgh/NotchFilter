#!/usr/bin/env bash

# Constant frequencies
./generate/constant.py output/constant.wav
./filter/notch.py output/constant.wav output/constant_filtered.wav
./visualize/waveform.py output/constant.wav output/constant_filtered.wav &

# Rising frequency
./generate/rising.py output/rising.wav
./filter/notch.py output/rising.wav output/rising_filtered.wav
./visualize/waveform.py output/rising.wav output/rising_filtered.wav &
