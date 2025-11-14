"""
PHY380 Assign 7
Jeryl Schudel
"""

import numpy as np
import math
import matplotlib.pyplot as plt

m = 2.0
k = 3.0
Cdamp = (4*(k/m))
h = 0.01
Vinit = 0
yinit = 2.0

def yprime(V, t):
    return V*t

def yEuler(y, V, t, step):
    return (y + yprime(V, t)*step)

def Vprime(C, V, y):
    return ((-C * V) - (y*(k/m)))

def VEuler(C, V, y, step):
    return (V + Vprime(C, V, y)*step)


t = np.arange(0,20+h,h)
#C = float(input("Please enter a damping value: ")) 


Clist = [0, 2.449, 1, 4] #decided to make subplots for the specific conditions instead

plt.figure(figsize = (20,12))
plt.suptitle("Harmonic Oscillator", fontsize=28, weight = 'bold')

for n, C in enumerate(Clist):
    if math.isclose((math.pow(C,2)), Cdamp, abs_tol=0.005) == True:
        label = "Critically damped"
#        print ("Damping is set as " + label)     #feedback no longer needed
    elif (math.pow(C,2)) == 0:
        label = "No damping"
#        print ("Damping is set as " + label)     #feedback no longer needed
    elif (math.pow(C,2)) < Cdamp:
        label = "Underdamped"
#        print ("Damping is set as " + label)     #feedback no longer needed 
    elif (math.pow(C,2)) > Cdamp:
        label = "Overdamped"
#        print ("Damping is set as " + label)     #feedback no longer needed
    y = [yinit]
    VE = [Vinit]
    for i in range(len(t)-1):
        VE.append(VEuler(C, VE[-1], y[-1], h))
        y.append(yEuler(y[-1], VE[-1], t[i], h))
    ax = plt.subplot(2,2,n+1)
    ax.plot(t, y)
    ax.set_title(label, fontsize=20)
    ax.set_xlabel('t (sec)', fontsize=16 )
    ax.set_ylabel('y (meters)', fontsize=16)
    ax.grid()

plt.tight_layout(pad=3.0, w_pad=0.6, h_pad=1.5)
plt.show()