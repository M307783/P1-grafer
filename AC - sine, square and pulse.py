# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 11:27:31 2025

@author: matil
"""


import numpy as np
import matplotlib.pyplot as plt


A = 2 #amplituden
f = 1 #frekvens
duration = 1 #sekunder
samples = duration*1000

x = np.linspace(0, duration, samples)
y_sin = A * np.sin(2 * np.pi * f * x)

plt.plot(x, y_sin, label="Sinusoidal wave",color="blue")

plt.axvline(x=0,ymin=0.5,ymax=0.95,color="green",label="Square wave")
plt.hlines(2, 0, 0.5,color="green")
plt.axvline(x=0.5,ymin=0.05,ymax=0.95,color="green")
plt.hlines(-2, 0.5, 1,color="green")
plt.axvline(x=1,ymin=0.05,ymax=0.5,color="green")

plt.hlines(0, 0, 0.15,color="brown")
plt.axvline(x=0.15,ymin=0.5,ymax=0.725,color="brown",label="Pulse wave")
plt.hlines(1, 0.15, 0.3,color="brown")
plt.axvline(x=0.3,ymin=0.5,ymax=0.725,color="brown")
plt.hlines(0, 0.3, 0.45,color="brown")
plt.axvline(x=0.45,ymin=0.5,ymax=0.725,color="brown")
plt.hlines(1, 0.45, 0.6,color="brown")
plt.axvline(x=0.6,ymin=0.5,ymax=0.725,color="brown")
plt.hlines(0, 0.6, 0.75,color="brown")
plt.axvline(x=0.75,ymin=0.5,ymax=0.725,color="brown")
plt.hlines(1, 0.75, 0.9,color="brown")
plt.axvline(x=0.9,ymin=0.5,ymax=0.725,color="brown")
plt.hlines(0, 0.9, 1,color="brown")

plt.xlabel("Time (s)")
plt.ylabel("Voltage [V]")
plt.legend()
plt.grid(True)
plt.show()
















"""

# Parameters
A = 1       # Amplitude
f = 1       # Frequency in Hz
duration = 1  # seconds
samples = 2000
duty_cycle = 0.4

# Generate time points and sine values in one step
x = np.linspace(0, duration, samples)
y = A * np.sin(2 * np.pi * f * x)

# Sine wave
y_sine = A * np.sin(2 * np.pi * f * x)

# Square wave (sign of sine)
y_square = A * np.sign(np.sin(2 * np.pi * f * x))

# Pulse wave (custom duty cycle)
# Use modulo to determine if we're in the "high" part of the cycle
y_pulse = np.array([A if (t % (1/f)) < duty_cycle * (1/f) else 0 for t in x])

# Plot all three
plt.plot(x, y_sine, label="Sine Wave")
plt.plot(x, y_square, label="Square Wave", linestyle="--")
plt.plot(x, y_pulse, label=f"Pulse Wave ({int(duty_cycle*100)}% duty)", linestyle=":")
plt.title("AC Current: Sine, Square, and Pulse Waves")
plt.xlabel("Time (s)")
plt.ylabel("Current (A)")
plt.legend()
plt.grid(True)
plt.show()

"""













