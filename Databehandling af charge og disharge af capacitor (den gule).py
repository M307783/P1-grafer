# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 15:29:24 2025

@author: matil
"""


import pandas as pd
pd.set_option('display.max_rows', 10) # begrænser hvor mange rækker der vises ad gangen hvilket er smart senere
pd.__version__ # Nuværende version af pandas

capacitor_charge_discharge = pd.read_csv('Data_capacitor_charge_discharge.csv', sep = ',')

#print(capacitor_charge_discharge)

#capacitor_charge_discharge.plot()



import matplotlib.pyplot as plt

#Charge
charge = capacitor_charge_discharge[(capacitor_charge_discharge["Time (s)"] >= 0.00000) & (capacitor_charge_discharge["Time (s)"] <= 0.00005)]



# Convert time to microseconds
charge['Time (µs)'] = charge['Time (s)'] * 1e6

# Plot using the actual data
plt.plot(charge['Time (µs)'], charge['Channel 2 (V)'], label="Charging")

# Labeling and styling
plt.xlabel("Time (µs)")
plt.ylabel("Voltage (V)")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

tau = 6.6   # time constant in microseconds
V0 = 2.0       # applied voltage in volts

t = np.linspace(0, 8 * tau, 500)

# Charging and discharging equations
V_charge = V0 * (1 - np.exp(-t / tau))
#V_discharge = V0 * np.exp(-t / tau)


# Plot
plt.figure()
plt.plot(t, V_charge, color = 'blue', label="Charging theoretical")
plt.plot(charge['Time (µs)'], charge['Channel 2 (V)'], color="green", label="Charging experimental")
#plt.plot(t, V_discharge, color = 'red', label="Discharging")
plt.xlabel("Time (µs)")
plt.ylabel("Voltage (V)")
plt.xlim(0,50)
plt.axvline(5 * tau, color='black', linestyle='--', label='5τ')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()














"""


#ax = charge.plot.scatter('Time (s)', 'Channel 2 (V)')
#ax.set_xlabel('Time (µs)')
#xticks = ax.get_xticks()
#ax.set_xticklabels([f"{x * 1e6:.0f}" for x in xticks])



#charge.plot.scatter('Time (s)','Channel 2 (V)')









#Discharge
discharge = capacitor_charge_discharge[(capacitor_charge_discharge["Time (s)"] >= 0.00005) & (capacitor_charge_discharge["Time (s)"] <= 0.00010)]

# Convert time to microseconds
discharge['Time (µs)'] = discharge['Time (s)'] * 1e6

# Plot using the actual data
plt.plot(discharge['Time (µs)'], discharge['Channel 2 (V)'], label="Discharging",color="red")

# Labeling and styling
plt.xlabel("Time (µs)")
plt.ylabel("Voltage (V)")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()



#discharge.plot.scatter('Time (s)','Channel 2 (V)')


#Begge plots i forlængelse af hinanden

import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots()

# Plot charge data
ax.scatter(charge['Time (s)'], charge['Channel 2 (V)'], color='blue', label='Charge')

# Plot discharge data
ax.scatter(discharge['Time (s)'], discharge['Channel 2 (V)'], color='red', label='Discharge')

# Add labels and legend
ax.set_xlabel('Time (s)')
ax.set_ylabel('Channel 2 (V)')
ax.set_title('Capacitor Charge and Discharge')
ax.legend()

# Show the plot
#plt.show()




#Begge plots oveni hinanden


import matplotlib.pyplot as plt


# Normalize time for charge and discharge
charge_time_zero = charge['Time (s)'] - charge['Time (s)'].iloc[0]
discharge_time_zero = discharge['Time (s)'] - discharge['Time (s)'].iloc[0]

# Create the plot
fig, ax = plt.subplots()

# Plot charge
ax.scatter(charge_time_zero, charge['Channel 2 (V)'], color='blue', label='Charge')

# Plot discharge
ax.scatter(discharge_time_zero, discharge['Channel 2 (V)'], color='red', label='Discharge')

# Labels and legend
ax.set_xlabel('Time since start (s)')
ax.set_ylabel('Channel 2 (V)')
ax.set_title('Normalized Capacitor Charge and Discharge')
ax.legend()

plt.show()



# Reset time to start at zero for each segment

charge['Time (µs)'] = (charge['Time (s)'] - charge['Time (s)'].iloc[0]) * 1e6
discharge['Time (µs)'] = (discharge['Time (s)'] - discharge['Time (s)'].iloc[0]) * 1e6

# Create a single plot
plt.plot(charge['Time (µs)'], charge['Channel 2 (V)'], label="Charging", color="blue")
plt.plot(discharge['Time (µs)'], discharge['Channel 2 (V)'], label="Discharging", color="red")

# Labeling and styling
plt.xlabel("Time (µs)")
plt.ylabel("Voltage (V)")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

"""

