#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Importing Packages
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as mpatches
from matplotlib import cm

# Setting up fixed values and variables
x = 203418.4 # Initial mass
a = (2*430)/x # Linear acceleration
t = math.sqrt(5/((1/2)*a)) # Linear acceleration time
tau = 14.61*2*430*np.sin(90*(np.pi/180)) # Torque
I = (1/2)*x*((6.7/2)**2+(6.7/2-0.47)**2) # Moment of inertia
alpha = tau/I # Angular acceleration
deltat = 0.605/alpha # Angular acceleration time
FCM = 2*0.135*(4*t+4*deltat) #Fuel consumption (mass)
FCV = FCM/1170 #Fuel consumption (volume) 
TFV = 11.53 #Total fuel left (volume)

def FuelBurnCalculator():
    global x , TFV , FCV , FCM
    i = 1
    
    while TFV > FCV:
        x = x - FCM
        a = (2*430)/x # Linear acceleration
        t = math.sqrt(5/((1/2)*a)) # Linear acceleration time
        tau = 14.61*2*430*np.sin(90*(np.pi/180)) # Torque
        I = (1/2)*x*((6.7/2)**2+(6.7/2-0.47)**2) # Moment of inertia
        alpha = tau/I # Angular acceleration
        deltat = 0.605/alpha # Angular acceleration time
        FCM = 2*0.135*(4*t+4*deltat) #Fuel consumption (mass)
        FCV = FCM/1170 #Fuel consumption (volume) 
        TFV = 11.53 - FCV #Total fuel left (volume)
        i += 1
        
        if TFV < FCV:
            print("Total number of artificial gravity generation cycles is " + str(i))

FuelBurnCalculator()



