#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing Packages
import numpy as np
import random
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as mpatches
from matplotlib import cm

# Setting up Spherical Earth to Plot
N = 50
phi = np.linspace(0, 2 * np.pi, N)
theta = np.linspace(0, np.pi, N)
theta, phi = np.meshgrid(theta, phi)

r_Earth = 6371  # Average radius of Earth [km]
r_GEO = r_Earth + 35786 # Setting GEO radius
X_Earth = r_Earth * np.cos(phi) * np.sin(theta)
Y_Earth = r_Earth * np.sin(phi) * np.sin(theta)
Z_Earth = r_Earth * np.cos(theta)

# Plotting Earth
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X_Earth, Y_Earth, Z_Earth, color='blue', alpha=1)
plt.title('Two-Body Orbits (GEO)')
ax.set_xlabel('X [km]')
ax.set_ylabel('Y [km]')
ax.set_zlabel('Z [km]')

# Plotting GEO
c, a = (r_GEO) , 1
x = (c + a*np.cos(theta)) * np.cos(phi)
y = (c + a*np.cos(theta)) * np.sin(phi)
z = a * np.sin(theta)
ax.plot_surface(x, y, z, rstride=5, cstride=5, color='r', edgecolors='r')

ax.view_init(30, 134)  # Changing viewing angle (adjust as needed)
fig = plt.figure()

# Add legend with proxy artists
col1, col2 = cm.jet(np.array([0.1, 0.9]))
col1_patch = mpatches.Patch(color=col1, label='Earth')
col2_patch = mpatches.Patch(color=col2, label='GEO')
ax.legend(handles=[col1_patch, col2_patch])


# Make axes limits
xyzlim = np.array([ax.get_xlim3d(), ax.get_ylim3d(),      
                   ax.get_zlim3d()]).T
XYZlim = np.asarray([min(xyzlim[0]), max(xyzlim[1])])
ax.set_xlim3d(XYZlim)
ax.set_ylim3d(XYZlim)
ax.set_zlim3d(XYZlim)
plt.show()


# In[ ]:




