"""
PHY380 Assign 7
Jeryl Schudel
"""

import math as m
import numpy as np
import creategrid as cg
import matplotlib.pyplot as plt

def dist(x,xp,y,yp):
    r = (((x-xp)**2)+((y-yp)**2))
    return m.sqrt(r)

def volt(q,r):    
    return (q / (r*4.0*8.854e-12*m.pi))

N = 50

Qdict = cg.qgrid(N)
Q = np.array(Qdict["charges"])
Loc = np.array(Qdict["coordinates"])

x = np.linspace(-10,10,200)
y = np.linspace(-20,20,400)

X,Y = np.meshgrid(x,y)

distv = np.vectorize(dist)
Vvect = np.vectorize(volt)

V = []
XP = []
YP = []

for item in Loc:
    XP.append(float(item[0]))
    YP.append(float(item[1]))

XP = np.array(XP)
YP = np.array(YP)

for i in range(len(Q)-1):
    R = []
    R.append(distv(X, XP[i], Y, YP[i]))
    for j in range(len(R)):
        V.append(np.where(R[j] > 0.25, Vvect(Q[i], R[j]), Vvect(Q[i], 0.25)))

#breakpoint()
Varray = np.array(sum(V))
Varray.real[abs(Varray.real) < 1e-4] = float(0.0)

vmin = np.min(Varray)
vmax = np.max(Varray)
vavg = np.average(Varray)
sca = vavg/0.1
my_levels = np.linspace(vmin, vmax, 50)

U, V = np.gradient(Varray)
C = np.sqrt(U**2 + V**2)


skip = (slice(None, None, 2), slice(None, None, 2))

fig, ax = plt.subplots(figsize=(15,12))
ax.set_title("Plot of Potential and Electric field for " + str(N) + " charges", fontsize=20)

contour = ax.contour(X, Y, Varray, levels=my_levels)
ax.quiver(X[skip], Y[skip], U[skip], V[skip], C[skip], scale=sca)
cbar = plt.colorbar(contour, orientation='horizontal', pad=0.1, shrink=0.8)
cbar.set_label('Field strength', rotation=0, labelpad=10)
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])


plt.show()
