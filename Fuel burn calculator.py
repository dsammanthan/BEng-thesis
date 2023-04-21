#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Importing Packages
import numpy as np
import matplotlib.pyplot as plt
import math

# Set initial values and variables
x = 203418.4 # Initial mass of set-up (kg)
a = (2*430)/x # Linear acceleration (m/s^2)
t = math.sqrt(5/((1/2)*a))# Linear acceleration time (s)
tau = 14.61*2*430*np.sin(90*(np.pi/180)) # Torque (Nm)
I = (1/2)*x*((6.7/2)**2+(6.7/2-0.47)**2) # Moment of inertia (kgm^2)
alpha = tau/I # Angular acceleration (rad/s^2)
deltat = 0.605/alpha # Angular acceleration time (s)
TFT = 4*t+4*deltat # Total firing time per cycle (s)
FCM = 2*0.135*TFT #Fuel consumption mass per cycle (kg)
FCV = FCM/1170 #Fuel consumption volume per cycle (m^3)
TFV = 11.53 #Total fuel left volume per cycle (m^3)

# Initialize arrays to store the values of x, FCV, and cycle count
x_values = [x]
FCV_values = [FCV]
FCM_values = [FCM]
TFV_values = [TFV]
t_values = [t] 
deltat_values = [deltat]
TFT_values = [TFT]
cycle_count = 0

# Loop until TFV is less than FCV
while TFV > FCV:
    global tau
    a = (2*430)/x
    t = math.sqrt(5/((1/2)*a))
    I = (1/2)*x*((6.7/2)**2+(6.7/2-0.47)**2)
    alpha = tau/I
    deltat = 0.605/alpha
    TFT = 4*t+4*deltat
    FCM = 2*0.135*TFT
    FCV = FCM/1170
    TFV -= FCV
    x -= FCM
    cycle_count += 1
    
    # Append the values of x, FCV, FCM, TFV, t, and delta t to their respective arrays
    x_values.append(x)
    FCV_values.append(FCV)
    FCM_values.append(FCM)
    TFV_values.append(TFV)
    t_values.append(t)
    deltat_values.append(deltat)
    TFT_values.append(TFT)
    
# Print the final value of x, TFV, and cycle count
print(f"Final value of x: {x}")
print(f"Final value of TFV: {TFV}")
print(f"Number of cycles: {cycle_count}")

# Plot the values of FCV, total mass, FCM and TFT over each cycle
time_values = np.arange(cycle_count+1)
plt.plot(time_values, FCV_values)
plt.xlabel('Artificial gravity generation cycles')
plt.ylabel('Volumetric fuel consumption per cycle ($\mathregular{m^{3}}$)')
plt.show()
plt.plot(time_values, TFT_values)
plt.xlabel('Artificial gravity generation cycles')
plt.ylabel('Total firing time per cycle (s)')
plt.show()
plt.plot(time_values, x_values)
plt.xlabel('Artificial gravity generation cycles')
plt.ylabel('Total set-up mass per cycle (kg)')
plt.show()
plt.plot(time_values, FCM_values)
plt.xlabel('Artificial gravity generation cycles')
plt.ylabel('Mass fuel consumption per cycle (kg)')
plt.show()

