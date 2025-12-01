# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 11:03:00 2025

@author: matil
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#DATA

pd.set_option('display.max_rows', 10) # begrænser hvor mange rækker der vises ad gangen hvilket er smart senere
pd.__version__ # Nuværende version af pandas

capacitor_charge_discharge = pd.read_csv('Data_capacitor_charge_discharge.csv', sep = ',')


#Charge
charge = capacitor_charge_discharge[(capacitor_charge_discharge["Time (s)"] >= 0.00000) & (capacitor_charge_discharge["Time (s)"] <= 0.00005)]

#Lav tid til mikrosekunder
charge['Time (µs)'] = charge['Time (s)'] * 1e6


#Discharge
discharge = capacitor_charge_discharge[(capacitor_charge_discharge["Time (s)"] >= 0.00005) & (capacitor_charge_discharge["Time (s)"] <= 0.00010)]

#Lav tid til mikrosekunder og ryk den til at starte ved 0
discharge['Time (µs)'] = (discharge['Time (s)'] - discharge['Time (s)'].iloc[0]) * 1e6


#THEORETICAL
tau_minus_procent = 5.8806
tau_plus_procent = 7.3326

tau = 6.6
V0 = 2.0

# Charging and discharging ligninger
V_charge = V0 * (1 - np.exp(-charge['Time (µs)'] / tau))
V_discharge = V0 * np.exp(-charge['Time (µs)'] / tau)

V_charge_minus_procent = V0 * (1 - np.exp(-charge['Time (µs)'] / tau_minus_procent))
V_charge_plus_procent = V0 * (1 - np.exp(-charge['Time (µs)'] / tau_plus_procent))

V_discharge_minus_procent = V0 * np.exp(-charge['Time (µs)'] / tau_minus_procent)
V_discharge_plus_procent = V0 * np.exp(-charge['Time (µs)'] / tau_plus_procent)


#PLOT

plt.figure()
plt.fill_between(
    charge['Time (µs)'],
    V_charge_minus_procent,
    V_charge_plus_procent,
    color="lime",
    alpha=0.3,
    label="Charging theoretical range"
)
plt.plot(charge['Time (µs)'], charge['Channel 2 (V)'], color="blue", label="Charging experimental")
plt.fill_between(
    charge['Time (µs)'],
    V_discharge_minus_procent,
    V_discharge_plus_procent,
    color="yellow",
    alpha=0.3,
    label="Discharging theoretical range"
)
plt.plot(discharge['Time (µs)'], discharge['Channel 2 (V)'], color="red", label="Discharging experimental")
plt.xlabel("Time (µs)")
plt.ylabel("Voltage (V)")
plt.xlim(0,20)
#plt.axvline(5 * tau, color='black', linestyle='--', label='5τ')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()



#DEVIATION
deviation_charge_tættest = charge['Channel 2 (V)'] - V_charge_plus_procent


plt.figure()
plt.plot(charge['Time (µs)'],deviation_charge_tættest)
plt.axhline(0, color='gray', linestyle='--')
plt.xlabel("Time (µs)")
plt.ylabel("Voltage Deviation (V)")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
#plt.show()



