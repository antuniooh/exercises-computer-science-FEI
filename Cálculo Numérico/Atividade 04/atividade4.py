#!/usr/bin/env python
# coding: utf-8

# In[41]:


#Nome: Antonio Gustavo Muniz
#RA: 22.119.001-0

#Calculo Numerico - Atividade 04


# In[18]:


import numpy as np
matriz_A=np.matrix([[50,200,160],[90,100,80],[180,250,120]])
matriz_B=([[11700],[7000],[14800]])
matriz_A_inv=np.linalg.inv(matriz_A)
sol=matriz_A_inv*matriz_B
print("Resultado do sistema linear")
print(sol)


# In[23]:


import numpy as np

matriz_A=np.matrix([[1,1,1],[0.07,0.08,0.09],[0.07,0.08,0.1]])
matriz_B=([[35000],[2830],[2960]])
matriz_A_inv=np.linalg.inv(matriz_A)
sol=matriz_A_inv*matriz_B
print("Resultado do sistema linear")
print(sol)


# In[56]:


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,6,10) # array com 20 pontos igualmente espaçados no intervalo 0 e 1
#-2.5 -x = sen(x)
y1 = -2.5 + 5*x
y2= np.sin(x)
# Pode-se incluir diversos gráficos
plt.plot(x,y1,x,y2) # gera dois gráficos simultaneamente
                                # um com os valores (x,y) e outro com (x,x**3)
                                # armazenando o resultado em uma variável
plt.grid() 


# In[21]:


from scipy.optimize import fsolve
import math

def y(x):
  f = x - 0.2*math.sin(x) - 0.5
  return f
print("O valor deu aproximadamente=...")
print(fsolve(y,0.5))


# In[4]:


from sympy import *
import numpy as np
x = np.array([i for i in range(-5,6,1)]).reshape((1,11))
y=(x+1)**2-np.exp(x);
print(x)
print(y)
print("\n")

x=Symbol('x')
def NewtonsMethod(x0):
    tolerance=0.000001
    d=diff(f(x),x)
    while True:
        x1 = x0 -(f(x0)/d.doit().subs({x:x0})) 
        t = abs(x1 -x0)
        if t < tolerance:
            break
        x0 = x1
    return x1

def f(x):
    return x**3 - 3*x**2 + 6*x -15
xi =3.5# ponto médio do intervalo
xr = NewtonsMethod(xi)
print('xi: ', xi)
print('x0: ', N(xr))
print("f(x0) = ", N(xr**3 - 3*xr**2 + 6*xr -15))
xi =4.5# ponto médio do intervalo
xr = NewtonsMethod(xi)
print('xi: ', xi)
print('x0: ', N(xr))
print("f(x0) = ", N(xr**3 - 3*xr**2 + 6*xr -15))


# In[ ]:




