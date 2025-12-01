# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 09:58:42 2025

@author: matil
"""






import pandas as pd
pd.set_option('display.max_rows', 10) # begrænser hvor mange rækker der vises ad gangen hvilket er smart senere
pd.__version__ # Nuværende version af pandas

capacitor_charge_discharge = pd.read_csv('Data_capacitor_charge_discharge.csv', sep = ',')

#Discharge
discharge = capacitor_charge_discharge[(capacitor_charge_discharge["Time (s)"] >= 0.00005) & (capacitor_charge_discharge["Time (s)"] <= 0.00010)]

# Shift time so it starts at zero and convert to microseconds
discharge['Time (µs)'] = (discharge['Time (s)'] - discharge['Time (s)'].iloc[0]) * 1e6




import numpy as np
import matplotlib.pyplot as plt

tau = 6.6   # time constant in microseconds
V0 = 2.0       # applied voltage in volts

t = np.linspace(0, 8 * tau, 500)

# Charging and discharging equations
#V_charge = V0 * (1 - np.exp(-t / tau))
V_discharge = V0 * np.exp(-discharge['Time (µs)'] / tau)

"""
# Plot
plt.figure()
plt.plot(t, V_discharge, color = 'yellow', label="Discharging")
plt.plot(discharge['Time (µs)'], discharge['Channel 2 (V)'], label="Discharging",color="red")
plt.xlabel("Time (µs)")
plt.ylabel("Voltage (V)")
plt.xlim(0,50)
plt.axvline(5 * tau, color='black', linestyle='--', label='5τ')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

"""


#PLOT FORSKELLEN MELLEM TEORETISK OG EKSPERIMENTELT

deviation = discharge['Channel 2 (V)'] - V_discharge
deviation_procent = (np.absolute(deviation/V_discharge))*100

# Plot deviation
plt.figure()
plt.plot(discharge['Time (µs)'], deviation_procent, color='orange', label='Deviation discharge (Experimental - Theoretical)')
plt.axhline(0, color='gray', linestyle='--')
plt.xlabel("Time (µs)")
plt.ylabel("Percentage deviation [%]")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()



