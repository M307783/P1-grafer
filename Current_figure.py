# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 11:27:25 2025

@author: Mira
"""
import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots(figsize=(6,6))

# axes
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# axis labels
ax.set_xlabel("Time", fontsize=14)
ax.set_ylabel("Voltage", fontsize=14)

# Direct current
ax.axhline(1, color='red', linestyle='-', linewidth=2, label='Direct current')

# ALternate current
t = np.linspace(0, 10, 500)
y = 2 * np.sin(t)
ax.plot(t, y, color='blue', linewidth=2, label='Alternate current')

# --- GRID ---
ax.grid(True, linestyle='--', color='gray', alpha=0.7)

# plot settings
ax.set_xlim(-1, 10)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.legend()

plt.show()