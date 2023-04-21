#!/usr/bin/env python
# coding: utf-8

# Importing packages
import matplotlib.pyplot as plt
import numpy as np

# Create the vectors X and Y
x1 = np.arange(1.5*np.pi,1.86*np.pi,0.02)   # start,stop,step
y1 = np.sin(x1)
x2 = np.arange(1.85*np.pi,2.15*np.pi,0.02)   # start,stop,step
y2 = np.sin(x2)
x3 = np.arange(2.15*np.pi,2.5*np.pi,0.02)   # start,stop,step
y3 = np.sin(x3)

# Create the plot
plt.plot(x1,y1,label='Pioneering phase')
plt.plot(x2,y2,label='Mature phase')
plt.plot(x3,y3,label='Mass phase')

# Add a title
plt.title('The three phases of space tourism')

# Add X and y Label
plt.xlabel('Time')
plt.ylabel('Number of tourists')
plt.xticks([])
plt.yticks([])

# Add a Legend
plt.legend()

# Show the plot
plt.show()
