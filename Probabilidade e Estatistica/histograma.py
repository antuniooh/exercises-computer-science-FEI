#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
base = [26, 39, 26, 29,34,27,28,30,29,32,34,30,29,32,21,24,23,29,30,36,31,37,34,30,27,28,33,28,32,34,27,34,29,31,27,32,33,36,37,30,
33,23,26,27,30,29,30,31,28,27
]
print(np.mean(base)) #calcula a média
print(np.median(base))# calcula a mediana
print(np.std(base, ddof = 1))#calcula o desvio padrão
print(stats.describe(base)) # descreve os resultados
plt.hist(base, bins = 'auto')
plt.title('Dados')
plt.ylabel('Frequência')
plt.xlabel('Valores')
plt.show()


# In[14]:


import seaborn as sns
sns.set(style="whitegrid")
ax = sns.boxplot(base)


# In[6]:


import seaborn as sns
sns.set(style="whitegrid")
base=[10,12,12,16,20,23,25,28]
ax = sns.boxplot(base)


# In[7]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
base = [5,2,11,8,3,8,7,4]
print(np.mean(base)) #calcula a média
print(np.median(base))# calcula a mediana
print(np.std(base, ddof = 1))#calcula o desvio padrão
print(stats.describe(base)) # descreve os resultados
h = np.histogram(base, bins = 'auto') #calcula o histograma
print(h)
plt.hist(base, bins = 'auto')
plt.title('Dados')
plt.ylabel('Frequência')
plt.xlabel('Valores')
plt.show()


# In[8]:


import seaborn as sns
sns.set(style="whitegrid")
ax = sns.boxplot(base)


# In[15]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
base = [7,5,6,6,4,6,8,6,9,3]
print(np.mean(base)) #calcula a média
print(np.median(base))# calcula a mediana
print(np.std(base, ddof = 1))#calcula o desvio padrão
import seaborn as sns
sns.set(style="whitegrid")
ax = sns.boxplot(base)


# In[16]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
base = [7,5,11,8,3,6,2,1,9,8]
print(np.mean(base)) #calcula a média
print(np.median(base))# calcula a mediana
print(np.std(base, ddof = 1))#calcula o desvio padrão
import seaborn as sns
sns.set(style="whitegrid")
ax = sns.boxplot(base)


# In[11]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
base = [64,49,54,64,97,66,76,44,71,89]
print(np.mean(base)) #calcula a média
print(np.median(base))# calcula a mediana
print(np.std(base, ddof = 1))#calcula o desvio padrão


# In[12]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
base = [70,72,71,55,60,62,46,77,86,71]
print(np.mean(base)) #calcula a média
print(np.median(base))# calcula a mediana
print(np.std(base, ddof = 1))#calcula o desvio padrão


# In[13]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
n=100
b1 = np.array([1.1,1.2,1.3,1.4,1.5])
b2=np.array([12,27,35,20,6])
b3=np.array([1.1**2,1.2**2,1.3**2,1.4**2,1.5**2])
base1=np.sum(b1*b2)
base2=np.sum(b2*b3)
med=base1/(n)
var=(1/(n-1))*(base2-(1/n)*base1**2)
desv=np.sqrt(var)
print(med)
print(var)
print(desv)


# In[8]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
base = [94,94,94,101,101,101,101,101,101,
        101, 101, 108, 108, 108, 108, 108, 108,
        108,108,108,108, 115, 115, 115, 115, 115, 115, 115,
        115, 122, 122, 122, 122, 122, 122, 122, 122, 122,122, 122, 129, 129, 129, 129, 129, 129,136,136,143,143]
print(np.mean(base)) #calcula a média
print(np.median(base))# calcula a mediana
print(np.std(base, ddof = 1))#calcula o desvio padrão
print(stats.describe(base)) # descreve os resultados
plt.hist(base, bins = 'auto')
plt.title('Dados')
plt.ylabel('Frequência')
plt.xlabel('Valores')
plt.show()


# In[13]:


base = [70,72,71,55,60,62,46,77,86,69,78,65,71]
print(np.mean(base)) #calcula a média
print(np.median(base))# calcula a mediana
print(np.std(base, ddof = 1))#calcula o desvio padrão
print(stats.describe(base)) # descreve os resultados
plt.hist(base, bins = 4)
plt.title('Dados')
plt.ylabel('Frequência')
plt.xlabel('Valores')
plt.show()


# In[10]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
base = [26,39,26,29,34,27,28,30,29,32]
print(np.mean(base)) #calcula a média
print(np.median(base))# calcula a mediana
print(np.std(base, ddof = 1))#calcula o desvio padrão
print(stats.describe(base)) # descreve os resultados
plt.hist(base, bins = 'auto')
plt.title('Dados')
plt.ylabel('Frequência')
plt.xlabel('Valores')
plt.show()


# In[4]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
base = [64,69,54,64,97,66,76,44,71,89]
print(np.mean(base)) #calcula a média
print(np.median(base))# calcula a mediana
print(np.std(base, ddof = 1))#calcula o desvio padrão
print(stats.describe(base)) # descreve os resultados


# In[5]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
base = [70,72,71,55,60,62,46,77,86,71]
print(np.mean(base)) #calcula a média
print(np.median(base))# calcula a mediana
print(np.std(base, ddof = 1))#calcula o desvio padrão
print(stats.describe(base)) # descreve os resultados


# ## Normalização dos Dados max min

# In[46]:


import random
random.seed(42) # define the seed (important to reproduce the results)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
data = pd.read_csv('iris.csv', header=(0))
print("Número de linhas e colunas:",data.shape)
data.head(25)


# In[47]:


corr = data.corr(method='pearson')
corr


# In[48]:


cov = data.cov()
cov


# In[49]:


data = data.to_numpy()
y = data[:,1]
x = data[:,0]

print(np.mean(x)) #calcula a média de x
print(np.mean(y)) #calcula a média de y
print(np.std(x))#calcula o desvio padrão de x
print(np.std(y))#calcula o desvio padrão de y   


# In[50]:


X_manual_scaled = (x-x.min(axis=0)) / (x.max(axis=0)-x.min(axis=0))
print(X_manual_scaled)


# In[51]:


from sklearn.preprocessing import StandardScaler
x=x.reshape(-1, 1)
scaler = MinMaxScaler()
scaler.fit(x)
# transform the test test
X = scaler.transform(x)
print('Dados transformados:')
print('Media: ', np.mean(X, axis = 0))
print('Desvio Padrao:', np.std(X, axis = 0))


# In[52]:


y=y.reshape(-1, 1)
scaler = MinMaxScaler()
scaler.fit(y)
# transform the test test
Y = scaler.transform(y)
print('Dados transformados:')
print('Media: ', np.mean(Y, axis = 0))
print('Desvio Padrao:', np.std(Y, axis = 0))


# In[ ]:




