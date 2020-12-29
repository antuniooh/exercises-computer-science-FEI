#!/usr/bin/env python
# coding: utf-8

# ## Exercício 3

# In[4]:


import numpy as np
x = np.linspace(2,3,5)
y = x * np.exp(2*x)
I = np.trapz(y,x)
print(I)


# In[5]:


import scipy.integrate as si
f= lambda x:x * np.exp(2*x)
i = si.quad(f, 2, 3)
print (i)


# In[6]:


erro=np.abs(I-i[0])
print(erro)


# In[ ]:




