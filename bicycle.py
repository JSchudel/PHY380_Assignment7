"""
PHY 380 Assign 7
Jeryl Schudel
"""

import numpy as np
import matplotlib.pyplot as plt

P = 400.0 #Power in watts
m = 70.0  #Mass in kilograms

def vprime(v):
    return (P/(m*v))

def Eulerstep(v, step):
    return (v + vprime(v)*step)

def RK2step(v, step):
    k1 = step*vprime(v)
    k2 = step*vprime(v + (k1/2))
    return (v + k2)

h = 0.1                     #Time step of 0.1sec
vinit = 4.0                 #Initial velocity of 4 m/s
t = np.arange(0,200+h,h)    #End at t=200sec

v = [vinit]
vRK2 = [vinit]

for i in range(len(t)-1):
    v.append(Eulerstep(v[-1], h))
    vRK2.append(RK2step(vRK2[-1], h))


plt.plot(t, v, label='Euler')
plt.plot(t, vRK2, color='green', label='RK2')
plt.xlabel('t (sec)')
plt.ylabel('v (meters per sec)')
plt.legend(loc="upper right", frameon=False)
plt.grid()
plt.show()
