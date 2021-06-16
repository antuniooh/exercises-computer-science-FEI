#!/usr/bin/env python
# coding: utf-8

# ## Teste de normalidade

# In[1]:


from scipy.stats import shapiro
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import datasets
data = pd.read_csv('iris.csv', header=(0))
print("Número de linhas e colunas:",data.shape)
data.head(25)


# In[3]:


# Analisar se a coluna sepal.length tem distribuição normal

data = data.to_numpy()
x = data[:,0]
# normalidade test
stat, p = shapiro(x)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpretação
alpha = 0.05
if p > alpha:
    print('Amostra Gaussiana (aceita H0)')
else:
    print('Amostra não Gausssiana (rejeita H0)')


# In[5]:


# Verificação atrav´s do histograma
plt.hist(x, bins = 'auto')
plt.title('Dados')
plt.ylabel('Frequência')
plt.xlabel('Valores')
plt.show()

