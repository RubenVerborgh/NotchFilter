#!/usr/bin/env bash
./generate/constant.py output/constant.wav
./filter/notch.py output/constant.wav output/constant_filtered.wav
./visualize/compare.py output/constant.wav output/constant_filtered.wav
