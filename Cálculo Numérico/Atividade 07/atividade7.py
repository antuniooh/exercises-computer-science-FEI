#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Antopnio Gustavo Muniz da Silva 22.119.001-0
#Atividade 07


# In[8]:


import sympy as sy
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.optimize import fsolve


X = [1,2,3,4]
X1 = np.array(X)
y = [15.4,10.8,7.5,5.3]
y1=np.log(y)
X1 = X1.reshape(-1, 1)
modelo = LinearRegression().fit(X1, y1)
b=np.exp(modelo.coef_)
a=np.exp(modelo.intercept_)

print(str(a) + "*(" + str(b) + ")^x" )
y2=a*b**X       
plt.scatter(X, y)
plt.plot(X, y2, color = 'red')
r1=y-y2; #diferença entre os pontos e a função ajustada


# In[1]:


import sympy as sy
import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
from scipy.interpolate import lagrange
x=[1,7,14]
y=[10.5, 17.7,35.2]
x = np.array(x)
y = np.array(y)
poly = lagrange(x, y)
Polynomial(poly).coef

print("Polinomio interpolador de lagrange: " + str(Polynomial(poly).coef[0]) +"*x^2 " 
      + str(Polynomial(poly).coef[1]) + "*x + " + str(Polynomial(poly).coef[2]))

print("Se a distancia for 4km, ele pagará R$ " + str(poly(4)))

z = np.polyfit(x, y, 2)
p = np.poly1d(z)
print("Valor quando tem 24 reais: " + str(np.roots(p-24)[1]))


# In[4]:


import scipy.integrate as si
import math
import numpy as np

f= lambda x:1/(1 + math.exp(x))
i = si.quad(f, 1, 2)
print(i)
print ("Trapézio : " + str(i[0]))

import numpy as np
x = np.linspace(1,2,4)
y = 1/(1 + np.exp(x))
IT = np.trapz(y,x)
I= si.quad(f, 1,2)
erro=np.abs(IT-I[0])
print(erro)


# In[ ]:




