#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Antonio Gustavo Muniz
#22.119.001-0

#Atividade 08


# In[8]:


import numpy as np
import matplotlib.pyplot as plt

def odeEuler(f,y0,t):
    y = np.zeros(len(t))
    y[0] = y0
    for n in range(0,len(t)-1):
        y[n+1] = y[n] + f(y[n],t[n])*(t[n+1] - t[n])
    return y

t = np.linspace(0,1,6)
y0 = 1
f = lambda y,t: (y**2) *(t)
y = odeEuler(f,y0,t)
print(y)

plt.plot(t,y,'b.-')
plt.legend(['Euler'])
plt.axis([0,1,1,2])
plt.grid(True)
plt.show()


# In[39]:


import sympy as sym
import scipy as sp
import matplotlib.pyplot as plt
x = sym.symbols('x')
f= sym.symbols('f', cls=sym.Function)
sol=sym.dsolve(f(x).diff(x)-(f(x)**2*x), 0)
sol


# In[40]:


constants = sym.solve([sol.rhs.subs(x,0) - 1])#condição inicial y(0)=1
constants


# In[43]:


C1= sym.symbols('C1')
sol = sol.subs(constants)
sol


# In[1]:


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
# function that returns dy/dt
def model(y,t):
    dydt = y - (2*t/y)
    return dydt
y0 = 2
t = np.linspace(1,1.5,10)
y = odeint(model,y0,t)
print(y)
# plot results
plt.plot(t,y)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.grid(True)
plt.show()


# In[4]:


import numpy as np
import matplotlib.pyplot as plt

def odeEuler(f,y0,t):
    y = np.zeros(len(t))
    y[0] = y0
    for n in range(0,len(t)-1):
        y[n+1] = y[n] + f(y[n],t[n])*(t[n+1] - t[n])
    return y

t = np.linspace(1,1.5,10)
y0 = 2
f = lambda y,t: y - (2*t/y)
y = odeEuler(f,y0,t)
print(y)

plt.plot(t,y,'b.-')
plt.legend(['Euler'])
plt.grid(True)
plt.show()


# In[ ]:




