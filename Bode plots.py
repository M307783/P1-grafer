

import math
import matplotlib.pyplot as plt
import numpy as np


def gainlp(omega,RC):
    gain = 1/(1+(RC*omega)**2)
    return gain
    
def phaselp(omega,RC):
    phase = -(np.atan(RC*omega))
    return phase

def gainhp(omega, RC):
    gain = omega/(omega**2+(1/RC)**0.5)**0.5
    return gain

def phasehp(omega,RC):
    phase = -(np.atan(RC*omega))
    return math.pi/2-np.atan(RC*omega)
    return phase

def bodeplot(RC):
    cutoff = 1/(RC*2*math.pi)
    omega = np.linspace(10**3,10**7,10000)
    frequency = omega/(2*math.pi)
    cutoffline = np.full(len(omega),-3)
    cutofffrequncy = np.full(len(omega), cutoff)
    gain = gainlp(omega,RC)
    phase = phaselp(omega,RC)
    dB = 20*np.log10(gain)
    fig, (ax1, ax2) = plt.subplots(2)
    ax1.plot(frequency,dB,label='Lowpass-filter gain')
    ax1.plot(frequency,cutoffline,linestyle='dashed')
    ax1.set_xscale('log')
    ax1.set_xlabel('gain [dB]')
    ax1.set_xticks([10**3,10**4,10**5,10**6],['kHz','10 kHz','100 kHz','MHz'])
    ax1.legend()
    ax1.grid()
    ax2.plot(frequency,phase,label='Lowpass-filter phase')
    ax2.plot(cutofffrequncy,phase,linestyle='dashed')
    ax2.set_ylabel('phase')
    ax2.set_xlabel('omega')
    ax2.set_xscale('log')
    ax2.grid()
    ax2.legend()
    plt.show

def bodeplothp(RC):
    cutoff = 1/RC
    omega = np.linspace(10**3,10**6,10000)
    cutoffline = np.full(len(omega),-3)
    cutofffrequncy = np.full(len(omega), 1/RC)
    gain = gainhp(omega,RC)
    phase = phasehp(omega,RC)
    dB = 20*np.log10(gain)
    fig, (ax1, ax2) = plt.subplots(2)
    ax1.plot(omega,dB,label='Highpass-filter gain')
    ax1.plot(omega,cutoffline,linestyle='dashed')
    ax1.set_xscale('log')
    ax1.set_xlabel('gain [dB]')
    ax1.legend()
    ax1.grid()
    ax2.plot(omega,phase,label='Highpass-filter phase')
    ax2.plot(cutofffrequncy,phase,linestyle='dashed')
    ax2.set_ylabel('phase')
    ax2.set_xlabel('omega')
    ax2.set_xscale('log')
    ax2.grid()
    ax2.legend()
    plt.show

bodeplot(0.0000066)
    
    




    