#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# In[3]:


def odeEuler(f,y0,t):
    y = np.zeros(len(t))
    y[0] = y0
    for n in range(0,len(t)-1):
        y[n+1] = y[n] + f(y[n],t[n])*(t[n+1] - t[n])
    return y


# In[5]:


t = np.linspace(0,1,6)
y0 = 1
f = lambda y,t: y + t*(y**2)
y = odeEuler(f,y0,t)
print(y)
plt.plot(t,y,'b.-')
plt.legend(['Euler'])
plt.axis([0,1,1,2])
plt.grid(True)
plt.show()


# In[ ]:




