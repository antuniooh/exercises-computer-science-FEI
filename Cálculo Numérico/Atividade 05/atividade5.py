#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Antonio Gustavo Muniz da Silva
#22.119.001 - 0


# In[30]:


import numpy as np
import matplotlib.pyplot as plt

# define os dados
x = np.array([1,2,3,4])
y = np.array([2.50,3.83,4.96,6.00])

n = np.size(x)
Sx= np.sum(x)
Sy=np.sum(y)
Sxy=np.sum(x*y)
Sxx=np.sum(x*x)
a1=(n*Sxy-Sx*Sy)/(n*Sxx-Sx**2) #Calcula o coeficiente a1 da reta
a0=(Sxx*Sy-Sxy*Sx)/(n*Sxx-Sx**2) #Calcula o coeficiente a0 da reta

# mostra os dados
plt.scatter(x, y, color = "b", marker = "o", s = 50)
# prediz os valores
y_pred = a0 + a1*x
print("y = " + str(a1) + "x +" +  str(a0))
# mostra a reta de regressão
plt.plot(x, y_pred, color = "r")
plt.xlabel('x', fontsize = 15)
plt.ylabel('y', fontsize = 15)
plt.show(True) 

#funcao que calcula o Residuo
def Residuo(x,y,b0,b1):
    n = len(y)
    RS = 0
    for i in range(0,n):
        y_pred=a0+a1*x[i]
        RS = RS + (y[i]-y_pred)**2
    return RS
print('RS:', Residuo(x,y,a0,a1))


# In[32]:


import sympy as sy
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

V = [2,3,4,5,7,10]
V = np.array(V)
I = [5.2,7.8,10.7,13,19.3,27.5]
V = V.reshape(-1, 1)
modelo = LinearRegression().fit(V, I)
print("y = " + str(modelo.coef_) + "x +" +  str(modelo.intercept_))
plt.scatter(V, I)
plt.plot(V, modelo.predict(V), color = 'red')
print()

# valor de i para V=3.5
yr=modelo.intercept_ + modelo.coef_ * (3.5)
print("Valor da corrente para V = 3.5")
print(yr)
print()

#valor de V para i =15
x=sy.Symbol('x')
y=modelo.intercept_ + modelo.coef_ * x -(15.00)
print("Valor da tensão para i = 15")
print(sy.solve(y))
print()

print("Resíduo:")
modelo._residues


# In[ ]:




