# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 09:46:14 2025

@author: matil
"""

import pandas as pd
pd.set_option('display.max_rows', 10) # begrænser hvor mange rækker der vises ad gangen hvilket er smart senere
pd.__version__ # Nuværende version af pandas

capacitor_charge_discharge = pd.read_csv('Data_capacitor_charge_discharge.csv', sep = ',')

#Charge
charge = capacitor_charge_discharge[(capacitor_charge_discharge["Time (s)"] >= 0.00000) & (capacitor_charge_discharge["Time (s)"] <= 0.00005)]

# Lav det til mikrosekunder
charge['Time (µs)'] = charge['Time (s)'] * 1e6

import numpy as np
import matplotlib.pyplot as plt

tau = 6.6
V0 = 2.0

t = np.linspace(0, 8 * tau, 500)

# Charging and discharging ligninger
V_charge = V0 * (1 - np.exp(-charge['Time (µs)'] / tau))
#V_discharge = V0 * np.exp(-t / tau)



# Plot
plt.figure()
plt.plot(t, V_charge, color = 'blue', label="Charging theoretical")
plt.plot(charge['Time (µs)'], charge['Channel 2 (V)'], color="lime", label="Charging experimental")
#plt.plot(t, V_discharge, color = 'red', label="Discharging")
plt.xlabel("Time (µs)")
plt.ylabel("Voltage (V)")
plt.xlim(0,50)
plt.axvline(5 * tau, color='black', linestyle='--', label='5τ')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()



#PLOT FORSKELLEN MELLEM TEORETISK OG EKSPERIMENTELT

deviation = charge['Channel 2 (V)'] - V_charge
deviation_procent = (np.absolute(deviation/V_charge))*100



# Plot deviation
plt.figure()
plt.plot(charge['Time (µs)'], deviation_procent, color='turquoise', label='Deviation charge (Experimental - Theoretical)')
plt.axhline(0, color='gray', linestyle='--')
plt.xlabel("Time (µs)")
plt.ylabel("Percentage deviation [%]")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()





