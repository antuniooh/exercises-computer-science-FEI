#!/usr/bin/env python
# coding: utf-8

# In[4]:


#1- f(x)=(x+1)2/3(x-3)2 com x variando de -4 até 4 com 50 pontos.

import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

x = np.linspace(-4,4,50)
y = (((x+1)**(2/3)) * ((x-3)**2))
plt.plot(x, y)


# In[17]:


from sympy import *
x=symbols('x')
eq= (cbrt((x+1))**2) * ((x-3)**2)
diff(eq, x)


# In[24]:


from sympy import *
x=symbols('x')
eq= (cbrt((x+1))**2) * ((x-3)**2)
diff(eq, x, 3)


# In[25]:


from sympy import *
x,y=symbols('x y')
y= (cbrt((x+1))**2) * ((x-3)**2)
integrate(y,x)


# In[23]:


from sympy import *
x,y=symbols('x y')
y= (cbrt((x+1))**2) * ((x-3)**2)
integrate(y,(x, -1, 2))


# In[13]:


import numpy as np

def calcula(x):
    return ((x**2 - 2*x)/(np.cos(x))) 
print("Resultado: ", calcula(np.sqrt(5)))


# In[23]:


from sympy import*
x=symbols('x')
expr=((x**2 - 2*x)/(cos(x)))
r=limit(expr,x,9)
print(r)


# In[14]:


from sympy import *
x=symbols('x')
eq=(((x**2) - (2*x))/(cos(x)))
diff(eq, x)


# In[37]:


import numpy as np

A=np.array([[1,0,1],[1,2,3],[1,2,4]])
print("A=\n", A)
B=np.array([[3,1,4],[1,2,1],[3,1,1]])
print("B=\n", B)

detA = np.linalg.det(A)
print(detA, "\n")

invB = np.linalg.inv(B)
print(invB, "\n")

aTrans = A.T
print(aTrans,"\n")
print(aTrans.shape, "\n")

M=np.dot(A, B)
print("M=\n", M,)

SUB = A - (4*B)
print("Sub=\n", SUB)


# In[44]:


import numpy as np

matrix = np.zeros((6,3))
array = np.arange(1,7).reshape(6,1)

print("M = ", (matrix + array))


# In[51]:


import numpy as np

M = np.random.randint(low=0, high=2,size=(10,10))
print("M = ", M)

sumM= np.sum(M, axis=0)
print('Soma dos valores das colunas: ',sumM)
print('Maior soma das colunas: ', np.max(sumM), ', coluna: ', np.argmax(sumM, axis=0))


# In[ ]:




