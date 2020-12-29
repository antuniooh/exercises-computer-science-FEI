#!/usr/bin/env python
# coding: utf-8

# ## Exercício 2

# In[4]:


import sympy as sy
import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
from scipy.interpolate import lagrange
x = [0,0.1250,0.2500,0.3750,0.5000]
y = [0,6.2400,7.7500,4.8500,0]

x = np.array(x)
y = np.array(y)
poly = lagrange(x, y)
Polynomial(poly).coef


# In[5]:


np.interp(0.2300, x, y)


# In[4]:


z = np.polyfit(x, y, 2)
print(z)
p = np.poly1d(z)
np.roots(p-24)

