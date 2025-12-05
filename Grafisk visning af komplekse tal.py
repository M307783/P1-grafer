# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 09:13:07 2025

@author: Mira
"""

import matplotlib.pyplot as plt

# Points and labels
points = [(2, 3), (-3, 1), (4, -2)]
labels = ["2+3j", "-3+1j", "4-2j"]

# Separate x and y coordinates
x, y = zip(*points)

# Plot
plt.figure(figsize=(6, 6))
plt.scatter(x, y, color='blue')

# Add labels near points
for (xi, yi), label in zip(points, labels):
    plt.text(xi + 0.1, yi + 0.1, label)

# Axes lines
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

plt.grid(True)
plt.xlabel("Real axis")
plt.ylabel("Imaginary axis")
plt.xlim(-5, 6)
plt.ylim(-3, 4)

plt.show()