
# coding: utf-8

# In[5]:


from math import *

x = float(input("Digite um número: "))

if x >= 5:
    y = (sqrt (log(x ** 3) + (3.14 ** 2) + 1) - log(x ** 5))/(exp(x) + (x ** 2) + (3 ** x))

    print("O valor de Y é: ", y)
    
else:
    y = (sin(x) ** 2) + (cos(x) ** 2) + abs(x)
    print("O valor de Y é: ", y)

