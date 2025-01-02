#!/usr/bin/env bash

# Constant frequencies
./generate/constant.py output/constant.wav
./filter/notch.py output/constant.wav output/constant_filtered.wav
./visualize/waveform.py output/constant.wav output/constant_filtered.wav &
./visualize/frequencies.py output/constant.wav output/constant_filtered.wav &
./visualize/polar.py output/constant.wav output/constant_filtered.wav &
