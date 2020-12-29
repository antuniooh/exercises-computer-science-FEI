#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import sympy as sy
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
from sklearn.linear_model import LinearRegression

def teste():
    x = [0, 5,10,15,20,25,30,35,40,45,50]
    y = [0, 20,22,39,42,45,47,45,40,39,0]
    i = np.trapz(y,x)

    x_2 = [0,10,20,30,40,50]
    y_2 = [0,34,50,52,36,0]
    i_2 = np.trapz(y_2,x_2)
    print(i + i_2)
    
teste()


# In[ ]:




