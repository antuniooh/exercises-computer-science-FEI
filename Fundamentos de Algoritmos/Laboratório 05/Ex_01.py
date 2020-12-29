#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = int(input("Digite o número: "))
resto = 0
resultado = []

while num != 0:
  resto = num % 2
  resto=str(resto)
  resultado.insert(0,resto)
  num = num // 2

print(resultado)


# In[ ]:




