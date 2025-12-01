# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 14:53:49 2025

@author: matil
"""

import numpy as np
import matplotlib.pyplot as plt

f = np.linspace(0, 2, 1000)
f_c = 1

lowpass = (f <= f_c)
highpass = (f > f_c)

#Low-pass filter
plt.plot(f, lowpass, "black")
plt.fill_between(f, lowpass, where=(f <= f_c), color='paleturquoise')
plt.axvline(f_c, color='red', ls='--')
plt.ylabel('Magnitude Response')
plt.xlabel('Frequency')
plt.xticks([f_c], ['$f_c$'])   # only show cutoff mark
plt.yticks([0, 1])              # only show 0 and 1
plt.text(0.3,0.5,"Passband")
plt.text(1.3,0.5,"Stopband")
plt.show()

#High-pass filter
plt.plot(f, highpass, "black")
plt.fill_between(f, highpass, where=(f > f_c), color='paleturquoise')
plt.axvline(f_c, color='red', ls='--')
plt.ylabel('Magnitude Response')
plt.xlabel('Frequency')
plt.xticks([f_c], ['$f_c$'])   # only show cutoff mark
plt.yticks([0, 1])              # only show 0 and 1
plt.text(0.3,0.5,"Stopband")
plt.text(1.3,0.5,"Passband")
plt.show()

