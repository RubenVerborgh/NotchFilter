#!/usr/bin/env bash
pushd $(dirname -- "$(readlink -f -- "$BASH_SOURCE")") > /dev/null

# constant frequencies
../generate/constant.py ../output/constant1.wav 440 1000 1500
../filter/notch.py ../output/constant1.wav ../output/constant1_filtered.wav 1000 30
../visualize/waveform.py ../output/constant1.wav ../output/constant1_filtered.wav &
../visualize/frequencies.py ../output/constant1.wav ../output/constant1_filtered.wav &
../visualize/polar.py ../output/constant1.wav ../output/constant1_filtered.wav 440 1000 1500 &
../visualize/polar_average.py ../output/constant1.wav ../output/constant1_filtered.wav 440 1000 1500 &
