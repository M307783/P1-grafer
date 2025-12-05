# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 10:06:10 2025

@author: Mira
"""
import numpy as np
import matplotlib.pyplot as plt

# complex number
z = 2 + 3j
x, y = z.real, z.imag

r = np.abs(z)
theta = np.angle(z)

fig, ax = plt.subplots(figsize=(6,6))

# modulus line
ax.plot([0, x], [0, y], 'k', zorder=1)

# projection lines
ax.plot([x, x], [0, y], 'k--', zorder=1)
ax.plot([0, x], [y, y], 'k--', zorder=1)

# scatter points
ax.scatter(x, y, color='red', s=80, zorder=5)
ax.scatter(x, 0, color='black', s=50, zorder=5)
ax.scatter(0, y, color='black', s=50, zorder=5)

# angle arc
arc_theta = np.linspace(0, theta, 100)
ax.plot(0.7*np.cos(arc_theta), 0.7*np.sin(arc_theta), 'b', zorder=2)

# annotations
ax.text(0.9*np.cos(theta/2), 0.9*np.sin(theta/2), 'Arg(z)', color='blue', fontsize=10)
ax.text(x+0.2, 0.15, 'x', fontsize=10, ha='center') 
ax.text(0.15, y+0.2, 'y', fontsize=10, va='center')
ax.text(0.6, 1.3, 'Modulus |z|', fontsize=10, rotation=55)
ax.text(x+0.2, y+0.2, 'z=x+yj', fontsize=10)
ax.text(1.5, -0.40, 'Real axis', fontsize=15)
ax.text(-0.4, 1.5, 'Imag axis', fontsize=15, rotation=90)

# axes
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# add ticks only for grid, but hide labels
ax.set_xticks(np.arange(-1, 5, 1))
ax.set_yticks(np.arange(-1, 5, 1))
ax.set_xticklabels([])
ax.set_yticklabels([])

# enable grid
ax.grid(True, linestyle='--', color='gray', alpha=1.0)

# plot settings
ax.set_xlim(-1, 4)
ax.set_ylim(-1, 4)
ax.set_aspect('equal')
ax.legend()

plt.show()