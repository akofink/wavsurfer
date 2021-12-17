#!/usr/bin/env python3

from numpy import append, iinfo, sin, linspace, int16, pi, zeros_like, ones_like, max as npmax
from scipy.io.wavfile import write
from scipy.signal import square, chirp

# import matplotlib.pyplot as plt

max_amplitude = iinfo(int16).max

A4 = 440.
A3 = 220.

samplerate = 44100;
duration_s = 5

t = linspace(0., duration_s, duration_s * samplerate, endpoint=False)
t_reversed = linspace(duration_s, 0., duration_s * samplerate, endpoint=False)
f_hz_t = linspace(A3, A4, duration_s * samplerate)
# signal = zeros_like(t)
# signal = ones_like(t)

signal = max_amplitude * square(2 * pi * A3 * t)
signal.append(max_amplitude * sin(2 * pi * f_hz_t * t_reversed))

# plt.plot(t, signal)
# plt.show()

write("example.wav", samplerate, signal.astype(int16))
