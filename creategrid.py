"""
PHY380 Assign 7
Created by: Dr. Pawlowski
"""

from numpy import arange,vstack,meshgrid,delete
from random import choice

def qgrid(n):
    '''Usage: data = qgrid(50)

    Assigns n charges to a qgrid at random.  qgrid returns a dictionary of two arrays:
    data['charges'] is an array of charges (in Coulombs)
    data['coordinates'] is an array of coordinate pairs corresponding to the location of each charge 
    (each pair a 2 element array, [x,y])
    '''

    h = 1
    x = arange(-10,10+h,h)
    y = arange(-20,20+h,h)

    nCharges = 50
    qCharge = [-1,-.5,-.25,.25,.5,1] #charges can have this sign

    coordinates = vstack(meshgrid(x,y)).reshape(2,-1).T

    q = []
    outCoordinates = []

    for i in range(nCharges):
        myCoorIndex = choice(range(len(coordinates)))
        q.append(choice(qCharge))
        outCoordinates.append(coordinates[myCoorIndex])
        coordinates = delete(coordinates,myCoorIndex,0)
    return {'charges':q,'coordinates':outCoordinates}

