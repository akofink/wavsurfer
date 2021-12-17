#!/usr/bin/env python3

from numpy import array, append, iinfo, sin, cos, linspace, int16, pi, zeros_like, ones_like, max as npmax
from scipy.io.wavfile import write
from scipy.signal import square, chirp

# import matplotlib.pyplot as plt

max_amplitude = iinfo(int16).max

A5 = 880.
A4 = 440.
A3 = 220.
A2 = 110.

samplerate = 44100;
duration_s = 10

t = linspace(0., duration_s, num=duration_s * samplerate)

# def cos_waveform(f_hz, duration_s=1, amplitude=max_amplitude):
#     return amplitude * cos(2 * pi * f_hz * t[:duration_s * samplerate])

# def sweep_amplitude(f_hz, from_A, to_A, duration_s=1):
#     amplitude = linspace(from_A, to_A, num=duration_s * samplerate)
#     return amplitude * cos(2 * pi * f_hz * t[:duration_s * samplerate])

# def sweep_hz(from_hz, to_hz, duration_s=1, method='linear'):
#     return max_amplitude * chirp(
#         t[:duration_s*samplerate],
#         f0=from_hz,
#         f1=to_hz,
#         t1=t[:duration_s*samplerate][-1],
#         method=method, # ‘linear’ | ‘quadratic’ | ‘logarithmic’ | ‘hyperbolic’
#     )

def waveform(f_hz, A=max_amplitude, duration_s=1, to_A=None, to_hz=None, method='linear'):
    to_hz = to_hz if to_hz is not None else f_hz
    amplitude = linspace(A, to_A, num=int(duration_s * samplerate)) if to_A is not None else A
    return amplitude * chirp(
        t[:int(duration_s*samplerate)],
        f0=f_hz,
        f1=to_hz,
        t1=t[:int(duration_s*samplerate)][-1],
        method=method, # ‘linear’ | ‘quadratic’ | ‘logarithmic’ | ‘hyperbolic’
    )

def append_all(*signals):
    waveform = array([])
    for signal in signals:
        waveform = append(waveform, signal)
    return waveform

signal = append_all(
    waveform(A2, A=0, to_A=max_amplitude, duration_s=0.1),
    waveform(A2, duration_s=2),
    waveform(A2, to_hz=A3, duration_s=5),
    waveform(A3, duration_s=2),
    waveform(A3, to_A=0, duration_s=0.1),
)

# signal = append_all(
#     waveform(A3, A=0, to_A=max_amplitude, duration_s=0.05),
#     waveform(A3, to_hz=A2, to_A=0, duration_s=5),
#     waveform(A2, to_hz=A3, A=0, to_A=max_amplitude, duration_s=5),
#     waveform(A3, to_A=0, duration_s=0.05),
# )

# center = 2 * samplerate
# plt.plot(t[center-1000:center+1000], signal[center-1000:center+1000])
# plt.savefig('waveform.png')
# plt.show()

write("example.wav", samplerate, signal.astype(int16))
