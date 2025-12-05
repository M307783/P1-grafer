# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 11:44:33 2025

@author: Mira
"""
import numpy as np
import matplotlib.pyplot as plt

# ---- RC værdier ----
R = 2000              # Ohm
C = 3.3e-9               # Farad
RC = R * C               # Tidskonstant

# ---- Tid ----
t = np.linspace(0, 20*RC, 2000)

# ---- Impulsrespons ----
h = (1/RC) * np.exp(-t/RC)

# ---- Plot ----
plt.figure(figsize=(8,4))
plt.plot(t, h, label="Impulsrespons h(t)")
plt.xlabel("t (s)")
plt.ylabel("h-low(t)")
plt.grid(True)
plt.legend()   
plt.tight_layout()
plt.show()

# ---- Impulsrespons high----
g = (-1/RC) * np.exp(-t/RC)

# ---- Plot ----
plt.figure(figsize=(8,4))
plt.plot(t, g, label="Impulsrespons h(t)")
plt.xlabel("t (s)")
plt.ylabel("h-high(t)")
plt.grid(True)
plt.legend()   
plt.tight_layout()
plt.show()