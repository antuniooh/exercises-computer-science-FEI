#!/usr/bin/env python
# coding: utf-8

# ## Distibuição conjunta em pyhton

# In[5]:


import numpy as np
# x = renda familiar em R$ 1000,00
# y = número de aparelhos de TV em cores
x=[1,2,3,1,3,2,3,1,2,3]
y=[2,1,3,1,3,3,2,1,2,2]
print(np.mean(x)) #calcula a média de x
print(np.mean(y)) #calcula a média de y
print(np.std(x))#calcula o desvio padrão de x
print(np.std(y))#calcula o desvio padrão de y      
print(np.cov(x,y))
correlacao = np.corrcoef(x, y)
print(correlacao)


# In[7]:


import seaborn as sns
sns.set(style="whitegrid")
ax = sns.boxplot(y)


# In[ ]:




