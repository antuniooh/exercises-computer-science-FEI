#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Antonio Gustavo Muniz
#22.119.001 - 0

#Atividade 10


# In[9]:


import random
random.seed(42)
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df = pd.read_csv("winequality-red.csv",) 
df.columns = ['fixed acidity', 'volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide',
              'total sulfur dioxide','density','pH','sulphates','alcohol','quality']
print("Número de linhas e colunas no conjunto de treinamento:", df.shape)
attributes = list(df.columns)
df.head(10)

df = df.to_numpy() #Transforma o dataframe em numpy


# In[8]:


y = df[:,0] 
x=df[:,11]
correlacao = np.corrcoef(x, y)
print("fixed acidity(y) x quality(x): ")
print(correlacao)
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
x = x.reshape(-1, 1)
result=lm.fit(x, y) #regressão linaer
print(result.intercept_) #valor de b
print(result.coef_)# valor do coeficiente angular
y_pred = lm.predict(x)
plt.scatter(x, y)
plt.plot(x, y_pred, color = 'red')


# In[10]:


y = df[:,2] 
x=df[:,7]
correlacao = np.corrcoef(x, y)
print("citric acid(y) x density(x): ")
print(correlacao)

from sklearn.linear_model import LinearRegression
lm = LinearRegression() 
x = x.reshape(-1, 1)
result=lm.fit(x, y) #regressão linaer
print(result.intercept_) #valor de b
print(result.coef_)# valor do coeficiente angular
y_pred = lm.predict(x)
plt.scatter(x, y)
plt.plot(x, y_pred, color = 'red')


# In[11]:



y = df[:,11] 
x=df[:,10]
correlacao = np.corrcoef(x, y)
print("quality(y) x alcohol(x): ")
print(correlacao)

from sklearn.linear_model import LinearRegression
lm = LinearRegression() 
x = x.reshape(-1, 1)
result=lm.fit(x, y) #regressão linaer
print(result.intercept_) #valor de b
print(result.coef_)# valor do coeficiente angular
y_pred = lm.predict(x)
plt.scatter(x, y)
plt.plot(x, y_pred, color = 'red')


# In[12]:


y = df[:,9] 
x=df[:,8]
correlacao = np.corrcoef(x, y)
print("sulfate(y) x pj(x): ")
print(correlacao)

from sklearn.linear_model import LinearRegression
lm = LinearRegression() 
x = x.reshape(-1, 1)
result=lm.fit(x, y) #regressão linaer
print(result.intercept_) #valor de b
print(result.coef_)# valor do coeficiente angular
y_pred = lm.predict(x)
plt.scatter(x, y)
plt.plot(x, y_pred, color = 'red')


# In[13]:


y = df[:,0] 
x=df[:,11]
import sympy as sy
import numpy as np
from sklearn.linear_model import LinearRegression
x = np.array(x)
x = x.reshape(-1, 1)
modelo = LinearRegression().fit(x, y)
print(modelo.intercept_)
print (modelo.coef_)
from sklearn.metrics import r2_score
R2 = r2_score(y, modelo.predict(x))
print('R2:', R2)


# In[ ]:




