#!/usr/bin/env bash

# Constant frequencies
./generate/constant.py output/constant.wav 440 554.37 880 1760
./filter/notch.py output/constant.wav output/constant_filtered.wav 554.37 30
./visualize/waveform.py output/constant.wav output/constant_filtered.wav &
./visualize/frequencies.py output/constant.wav output/constant_filtered.wav &
./visualize/polar.py output/constant.wav output/constant_filtered.wav &
