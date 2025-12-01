# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 10:55:42 2025

@author: matil
"""

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_rows",10)
pd.__version__

data = pd.read_csv("Data til bode plots - high-pass.csv", sep = ",")


plt.figure()
plt.plot(data["Frequency (Hz)"], data["Channel 2 Magnitude (dB)"])
plt.xscale("log", base=10)
plt.xticks([10**3,10**4,10**5,10**6],["1kHz","10kHz","100kHz","1MHz"])
#plt.plot(data["Frequency (Hz)"], data["Channel 2 Phase (deg)"])
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.axvline(24114.38531, color='black', linestyle='--', label='Cutoff frequency')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure()
#plt.plot(data["Frequency (Hz)"], data["Channel 2 Magnitude (dB)"])
plt.plot(data["Frequency (Hz)"], data["Channel 2 Phase (deg)"])
plt.xscale("log", base=10)
plt.xticks([10**3,10**4,10**5,10**6],["1kHz","10kHz","100kHz","1MHz"])
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (deg)")
plt.axvline(24114.38531, color='black', linestyle='--', label='Cutoff frequency')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()




fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(data["Frequency (Hz)"],data["Channel 2 Magnitude (dB)"],label='High-pass-filter gain',color="green")
#ax1.axvline(24114.38531, color='black', linestyle='--', label='Cutoff frequency')
#ax1.text(24114.38531, ax1.get_ylim()[0]-4, r'$f_c$')
ax1.set_xscale('log')
ax1.set_ylabel('Gain [dB]')
ax1.set_xticks([10**3,10**4,10**5,10**6],['1 kHz','10 kHz','100 kHz','1 MHz'])
ax1.legend()
ax1.grid()
ax2.plot(data["Frequency (Hz)"],data["Channel 2 Phase (deg)"],label='High-pass-filter phase',color="green")
#ax2.axvline(24114.38531, color='black', linestyle='--', label='Cutoff frequency')
#ax2.text(24114.38531, ax1.get_ylim()[0]+14, r'$f_c$')
ax2.set_ylabel('Phase [deg]')
ax2.set_xlabel('Frequency')
ax2.set_xscale('log')
ax2.set_xticks([10**3,10**4,10**5,10**6],['1 kHz','10 kHz','100 kHz','1 MHz'])
ax2.grid()
ax2.legend()
plt.show

