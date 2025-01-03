#!/usr/bin/env bash
pushd $(dirname -- "$(readlink -f -- "$BASH_SOURCE")") > /dev/null

# Rising frequency
../generate/rising.py ../output/rising.wav 0 22050
../filter/notch.py ../output/rising.wav ../output/rising_filtered.wav 1000 1
../visualize/waveform.py ../output/rising.wav ../output/rising_filtered.wav &
../visualize/frequencies.py ../output/rising.wav ../output/rising_filtered.wav &
../visualize/polar.py ../output/rising.wav ../output/rising_filtered.wav 1000 2000 &
../visualize/polar_average.py ../output/rising.wav ../output/rising_filtered.wav 1000 2000 &
