# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 13:16:04 2025

@author: matil
"""

import math
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd


def gainlp(frequency,RC):
    gain = 20*np.log10(1/(np.sqrt(1+(RC*frequency*2*math.pi)**2)))
    return gain
    
def phaselp(frequency,RC):
    phase = np.rad2deg(-(np.atan(RC*frequency*2*math.pi)))
    return phase

def gainhp(frequency,RC):
    gain = 20*np.log10((frequency*2*math.pi)/((frequency*2*math.pi)**2+(1/RC)**2)**0.5)
    return gain

def phasehp(frequency,RC):
    phase = np.rad2deg((math.pi/2)-np.atan(RC*frequency*2*math.pi))
    return phase

pd.set_option("display.max_rows",10)
pd.__version__

datahp = pd.read_csv("Data til bode plots - high-pass.csv", sep = ",")

datalp = pd.read_csv("Data til bode plots.csv", sep = ",")

#print(datalp.head(n=5))


def deviation_gain_lp(RC):
    deviation = datalp["Channel 2 Magnitude (dB)"]-gainlp(datalp["Frequency (Hz)"], RC)
    deviation_procent = (np.absolute(deviation/gainlp(datalp["Frequency (Hz)"], RC)))*100
    return deviation_procent


def deviation_phase_lp(RC):
    deviation = datalp["Channel 2 Phase (deg)"]-phaselp(datalp["Frequency (Hz)"], RC)
    deviation_procent = (np.absolute(deviation/phaselp(datalp["Frequency (Hz)"], RC)))*100
    return deviation_procent




#LOW-PASS - AFVIGELSE
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(datalp["Frequency (Hz)"],(datalp["Channel 2 Magnitude (dB)"]-gainlp(datalp["Frequency (Hz)"], 0.0000066)),label='Deviation gain low-pass',color="blue")
ax1.set_xscale('log')
ax1.set_ylabel('Gain [dB]')
ax1.set_xticks([10**3,10**4,10**5,10**6],['1 kHz','10 kHz','100 kHz','1 MHz'])
ax1.legend()#fontsize=8)
ax1.grid()
ax2.plot(datalp["Frequency (Hz)"],(datalp["Channel 2 Phase (deg)"]-phaselp(datalp["Frequency (Hz)"], 0.0000066)),label='Deviation phase low-pass',color="blue")
ax2.set_ylabel('Phase[deg]')
ax2.set_xlabel('Frequency')
ax2.set_xscale('log')
ax2.set_xticks([10**3,10**4,10**5,10**6],['1 kHz','10 kHz','100 kHz','1 MHz'])
ax2.grid()
ax2.legend()#fontsize=8)
plt.show




#LOW-PASS - PROCENT AFVIGELSE
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(datalp["Frequency (Hz)"],deviation_gain_lp(0.0000066),label='Percentage deviation gain low-pass',color="blue")
ax1.set_xscale('log')
ax1.set_ylabel('Deviation[%]')
ax1.set_xticks([10**3,10**4,10**5,10**6],['1 kHz','10 kHz','100 kHz','1 MHz'])
ax1.legend()#fontsize=8)
ax1.grid()
ax2.plot(datalp["Frequency (Hz)"],deviation_phase_lp(0.0000066),label='Percentage deviation phase low-pass',color="blue")
ax2.set_ylabel('Deviation[%]')
ax2.set_xlabel('Frequency')
ax2.set_xscale('log')
ax2.set_xticks([10**3,10**4,10**5,10**6],['1 kHz','10 kHz','100 kHz','1 MHz'])
ax2.grid()
ax2.legend()#fontsize=8)
plt.show



def deviation_gain_hp(RC):
    deviation = datahp["Channel 2 Magnitude (dB)"]-gainhp(datahp["Frequency (Hz)"], RC)
    deviation_procent = (np.absolute(deviation/gainhp(datahp["Frequency (Hz)"], RC)))*100
    return deviation_procent

def deviation_phase_hp(RC):
    deviation = datahp["Channel 2 Phase (deg)"]-phasehp(datahp["Frequency (Hz)"], RC)
    deviation_procent = (np.absolute(deviation/phasehp(datalp["Frequency (Hz)"], RC)))*100
    return deviation_procent



#HIGH-PASS - AFVIGELSE
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(datahp["Frequency (Hz)"],(datahp["Channel 2 Magnitude (dB)"]-gainhp(datahp["Frequency (Hz)"], 0.0000066)),label='Deviation gain high-pass',color="red")
ax1.set_xscale('log')
ax1.set_ylabel('Gain [dB]')
ax1.set_xticks([10**3,10**4,10**5,10**6],['1 kHz','10 kHz','100 kHz','1 MHz'])
ax1.legend()#fontsize=8)
ax1.grid()
ax2.plot(datahp["Frequency (Hz)"],(datahp["Channel 2 Phase (deg)"]-phasehp(datahp["Frequency (Hz)"], 0.0000066)),label='Deviation phase high-pass',color="red")
ax2.set_ylabel('Phase[deg]')
ax2.set_xlabel('Frequency')
ax2.set_xscale('log')
ax2.set_xticks([10**3,10**4,10**5,10**6],['1 kHz','10 kHz','100 kHz','1 MHz'])
ax2.grid()
ax2.legend()#fontsize=8)
plt.show




#HIGH-PASS - PROCENT AFVIGELSE
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(datahp["Frequency (Hz)"],deviation_gain_hp(0.0000066),label='Percentage deviation gain high-pass',color="red")
ax1.set_xscale('log')
ax1.set_ylabel('Deviation[%]')
ax1.set_xticks([10**3,10**4,10**5,10**6],['1 kHz','10 kHz','100 kHz','1 MHz'])
ax1.legend()#fontsize=8)
ax1.grid()
ax2.plot(datahp["Frequency (Hz)"],deviation_phase_hp(0.0000066),label='Percentage deviation phase high-pass',color="red")
ax2.set_ylabel('Deviation[%]')
ax2.set_xlabel('Frequency')
ax2.set_xscale('log')
ax2.set_xticks([10**3,10**4,10**5,10**6],['1 kHz','10 kHz','100 kHz','1 MHz'])
ax2.grid()
ax2.legend()#fontsize=8)
plt.show











































"""



#LOW-PASS
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(datalp["Frequency (Hz)"],datalp["Channel 2 Magnitude (dB)"],label='Low-pass-filter experimental gain ',color="orange")
ax1.plot(datalp["Frequency (Hz)"],gainlp(datalp["Frequency (Hz)"],0.0000066),label='Low-pass-filter theoretical gain',color="blue")
#ax1.axvline(24114.38531, color='black', linestyle='--', label='Theoretical cutoff frequency')
#ax1.plot(data["Frequency (Hz)"],np.full(len(data["Frequency (Hz)"]),-3),color='red', linestyle='--', label='Cutoff frequency')
#ax1.text(24114.38531, ax1.get_ylim()[0]-4, r'$f_c$')
ax1.set_xscale('log')
ax1.set_ylabel('Gain [dB]')
ax1.set_xticks([10**3,10**4,10**5,10**6],['1 kHz','10 kHz','100 kHz','1 MHz'])
ax1.legend()#fontsize=8)
ax1.grid()
ax2.plot(datalp["Frequency (Hz)"],datalp["Channel 2 Phase (deg)"],label='Low-pass-filter experimental phase',color="orange")
ax2.plot(datalp["Frequency (Hz)"],phaselp(datalp["Frequency (Hz)"],0.0000066),label='Low-pass-filter theoretical phase',color="blue")
#ax2.axvline(24114.38531, color='black', linestyle='--', label='Theoretical cutoff frequency')
#ax2.plot(data["Frequency (Hz)"],np.full(len(data["Frequency (Hz)"]),-45),color='red', linestyle='--', label='Cutoff frequency')
#ax2.text(24114.38531, ax1.get_ylim()[0]-66, r'$f_c$')
ax2.set_ylabel('Phase [deg]')
ax2.set_xlabel('Frequency')
ax2.set_xscale('log')
ax2.set_xticks([10**3,10**4,10**5,10**6],['1 kHz','10 kHz','100 kHz','1 MHz'])
ax2.grid()
ax2.legend()#fontsize=8)
plt.show


#HIGH-PASS
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(datahp["Frequency (Hz)"],datahp["Channel 2 Magnitude (dB)"],label='High-pass-filter experimental gain ',color="green")
ax1.plot(datahp["Frequency (Hz)"],gainhp(datahp["Frequency (Hz)"],0.0000066),label='High-pass-filter theoretical gain',color="red")
#ax1.axvline(24114.38531, color='black', linestyle='--', label='Theoretical cutoff frequency')
#ax1.plot(data["Frequency (Hz)"],np.full(len(data["Frequency (Hz)"]),-3),color='red', linestyle='--', label='Cutoff frequency')
#ax1.text(24114.38531, ax1.get_ylim()[0]-4, r'$f_c$')
ax1.set_xscale('log')
ax1.set_ylabel('Gain [dB]')
ax1.set_xticks([10**3,10**4,10**5,10**6],['1 kHz','10 kHz','100 kHz','1 MHz'])
ax1.legend()#fontsize=8)
ax1.grid()
ax2.plot(datahp["Frequency (Hz)"],datahp["Channel 2 Phase (deg)"],label='High-pass-filter experimental phase',color="green")
ax2.plot(datahp["Frequency (Hz)"],phasehp(datahp["Frequency (Hz)"],0.0000066),label='High-pass-filter theoretical phase',color="red")
#ax2.axvline(24114.38531, color='black', linestyle='--', label='Theoretical cutoff frequency')
#ax2.plot(data["Frequency (Hz)"],np.full(len(data["Frequency (Hz)"]),-45),color='red', linestyle='--', label='Cutoff frequency')
#ax2.text(24114.38531, ax1.get_ylim()[0]-66, r'$f_c$')
ax2.set_ylabel('Phase [deg]')
ax2.set_xlabel('Frequency')
ax2.set_xscale('log')
ax2.set_xticks([10**3,10**4,10**5,10**6],['1 kHz','10 kHz','100 kHz','1 MHz'])
ax2.grid()
ax2.legend()#fontsize=8)
plt.show








#LOW-PASS - Interval
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(datalp["Frequency (Hz)"],datalp["Channel 2 Magnitude (dB)"],label='Low-pass-filter experimental gain ',color="orange")
#ax1.plot(datalp["Frequency (Hz)"],gainlp(datalp["Frequency (Hz)"],0.0000058806),label='Low-pass-filter theoretical gain',color="blue")
#ax1.plot(datalp["Frequency (Hz)"],gainlp(datalp["Frequency (Hz)"],0.0000073326),label='Low-pass-filter theoretical gain',color="blue")
ax1.fill_between(
    datalp["Frequency (Hz)"],
    gainlp(datalp["Frequency (Hz)"],0.0000058806),
    gainlp(datalp["Frequency (Hz)"],0.0000073326),
    color="blue",
    alpha=0.70,
    label="Gain theoretical range"
)
ax1.set_xscale('log')
ax1.set_ylabel('Gain [dB]')
ax1.set_xticks([10**3,10**4,10**5,10**6],['1 kHz','10 kHz','100 kHz','1 MHz'])
ax1.legend(fontsize=8.5)
ax1.set_xlim(1000, 10**6)
ax1.grid()

ax2.plot(datalp["Frequency (Hz)"],datalp["Channel 2 Phase (deg)"],label='Low-pass-filter experimental phase',color="orange")
#ax2.plot(datalp["Frequency (Hz)"],phaselp(datalp["Frequency (Hz)"],0.0000058806),label='Low-pass-filter theoretical phase',color="blue")
#ax2.plot(datalp["Frequency (Hz)"],phaselp(datalp["Frequency (Hz)"],0.0000073326),label='Low-pass-filter theoretical phase',color="blue")
ax2.fill_between(
    datalp["Frequency (Hz)"],
    phaselp(datalp["Frequency (Hz)"],0.0000058806),
    phaselp(datalp["Frequency (Hz)"],0.0000073326),
    color="blue",
    alpha=0.70,
    label="Phase theoretical range"
)
ax2.set_ylabel('Phase [deg]')
ax2.set_xlabel('Frequency')
ax2.set_xscale('log')
ax2.set_xticks([10**3,10**4,10**5,10**6],['1 kHz','10 kHz','100 kHz','1 MHz'])
ax2.hlines(-90,1000,10**6,colors="crimson", linestyles='dashed', label='-90 degrees')
ax2.grid()
ax2.legend(fontsize=8.5)
ax2.set_xlim(1000, 10**6)
plt.show



#HIGH-PASS - Interval
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(datahp["Frequency (Hz)"],datahp["Channel 2 Magnitude (dB)"],label='High-pass-filter experimental gain ',color="green")
ax1.fill_between(
    datahp["Frequency (Hz)"],
    gainhp(datahp["Frequency (Hz)"],0.0000058806),
    gainhp(datahp["Frequency (Hz)"],0.0000073326),
    color="red",
    alpha=0.5,
    label="Gain theoretical range"
)
ax1.set_xscale('log')
ax1.set_ylabel('Gain [dB]')
ax1.set_xticks([10**3,10**4,10**5,10**6],['1 kHz','10 kHz','100 kHz','1 MHz'])
ax1.legend(fontsize=9)
ax1.set_xlim(1000, 10**6)
ax1.grid()

ax2.plot(datahp["Frequency (Hz)"],datahp["Channel 2 Phase (deg)"],label='High-pass-filter experimental phase',color="green")
ax2.fill_between(
    datahp["Frequency (Hz)"],
    phasehp(datahp["Frequency (Hz)"],0.0000058806),
    phasehp(datahp["Frequency (Hz)"],0.0000073326),
    color="red",
    alpha=0.5,
    label="Phase theoretical range"
)
ax2.set_ylabel('Phase [deg]')
ax2.set_xlabel('Frequency')
ax2.set_xscale('log')
ax2.set_xticks([10**3,10**4,10**5,10**6],['1 kHz','10 kHz','100 kHz','1 MHz'])
#ax2.hlines(90,1000,10**6,colors="crimson", linestyles='dashed', label='-90 degrees')
ax2.grid()
ax2.legend(fontsize=9)
ax2.set_xlim(1000, 10**6)
plt.show




"""


















"""
plt.plot(datalp["Frequency (Hz)"],deviation_gain_lp(0.0000066))
plt.plot(datalp["Frequency (Hz)"],deviation_gain_lp(0.0000062073),color="red")
plt.plot(datalp["Frequency (Hz)"],deviation_gain_lp(0.0000069993),color="lime")
plt.axvline(24114.38531, color='black', linestyle='--', label='Cutoff frequency')
plt.xscale("log")
plt.show()
"""























"""

fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(data["Frequency (Hz)"],data["Channel 2 Magnitude (dB)"],label='High-pass-filter gain')
#ax1.axvline(24114.38531, color='black', linestyle='--', label='Cutoff frequency')
#ax1.text(24114.38531, ax1.get_ylim()[0]-4, r'$f_c$')
ax1.set_xscale('log')
ax1.set_ylabel('Gain [dB]')
ax1.set_xticks([10**3,10**4,10**5,10**6],['1 kHz','10 kHz','100 kHz','1 MHz'])
ax1.legend()
ax1.grid()
ax2.plot(data["Frequency (Hz)"],data["Channel 2 Phase (deg)"],label='High-pass-filter phase')
#ax2.axvline(24114.38531, color='black', linestyle='--', label='Cutoff frequency')
#ax2.text(24114.38531, ax1.get_ylim()[0]+14, r'$f_c$')
ax2.set_ylabel('Phase [deg]')
ax2.set_xlabel('Frequency')
ax2.set_xscale('log')
ax2.set_xticks([10**3,10**4,10**5,10**6],['1 kHz','10 kHz','100 kHz','1 MHz'])
ax2.grid()
ax2.legend()
plt.show


"""



