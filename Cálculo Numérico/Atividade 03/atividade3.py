#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#ANTONIO GUSTAVO MUNIZ DA SILVA
#22.119.001 - 0


# In[11]:


import numpy as np
x = np.array([i for i in range(-4,5,1)]).reshape((1,9))
y=np.cos(x) + x**2 + 2*x - 2
print(x)
print(y)


# In[4]:


import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
from scipy.optimize import fsolve
from math import exp
from sympy import *

x = np.linspace(-4,4,20)
y1 = np.sin(x)
y2= x**2 + x - 2

line_1 = plt.plot(x,y1)
line_2=plt.plot(x,y2)

plt.setp(line_1,color='blue',linewidth = 2)
plt.setp(line_2,color='red',linewidth = 2)

plt.grid(True)

def y(x):
    f= np.sin(x) + (-x**2) - x + 2
    return f
R=fsolve(y,-1.5)
print(R)
R=fsolve(y,1.2)
print(R)

xValue = np.array([i for i in range(-4,5,1)]).reshape((1,9))
yValue=np.sin(xValue) - xValue**2 - xValue + 2
print(xValue)
print(yValue)

x=Symbol('x')
def NewtonsMethod(x0):
    d=diff(f(x),x)
    for i in range(0,5):
        x1 = x0 - (f(x0)/d.doit().subs({x:x0}))
        x0 = x1
    return x1
def f(x):
    return sin(x) - x**2 - x + 2

xi = -2.5
xr = NewtonsMethod(xi)
print('xi: ', xi)
print('x0: ', N(xr))
print("f(x0) = ", N(sin(xr) -xr**2 - xr + 2))

print("\n")
xi = 0.5
xr = NewtonsMethod(xi)
print('xi: ', xi)
print('x0: ', N(xr))
print("f(x0) = ", N(sin(xr) -xr**2 - xr + 2))


# In[8]:


import matplotlib.pyplot as plt
import numpy as np
from numpy import roots
get_ipython().run_line_magic('matplotlib', 'inline')

x = np.linspace(-2,4,20)
y1 = (x**5 - 3.5*(x**4) + 2.75*(x**3) + 2.125*(x**2) - (3.975*x) + 1.25 )
line_1 = plt.plot(x,y1)
plt.setp(line_1,color='red',linewidth = 2, linestyle = '--')
plt.grid(True)

coeficientes=[1,-3.5,2.75, 2.125, -3.975, 1.25]
raiz=roots(coeficientes)
print("Raiz da equação x^5 - 3.5x^4 + 2.75x^3 + 2.125x^2 -3.975x + 1.25")
print(raiz)


# In[ ]:





# In[ ]:





# In[ ]:




