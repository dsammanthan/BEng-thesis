#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np

# Create the vectors
Pi = ((np.exp**(yi ** 2))*(s ** 2))/s 
Q = 1 + 1/(2*(s**2))
G = 1/(2*(s**2))
Z = 1 + np.exp*


# Create the plot
plt.plot(Cl,alpha,label='Coefficient of lift')
plt.plot(Cd,alpha,label='Coefficient of drag')

# Add a title
plt.title('Coefficients of lift & drag against angle of attack')

# Add X and y Label
plt.xlabel('Angle of attack')
plt.ylabel('Coefficient of lift')

# Add a Legend
plt.legend()

# Show the plot
plt.show()


# In[ ]:




