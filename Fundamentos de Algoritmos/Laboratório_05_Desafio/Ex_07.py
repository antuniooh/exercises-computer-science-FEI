#!/usr/bin/env python
# coding: utf-8

# In[6]:


limite = int(input("Digite o limite: "))
lista =[]
p =2

for x in range(2, limite):
    lista.append(x)

for x in range(len(lista)):
    if lista[x] % 2 == 0 and lista[x] != 2:
        lista[x] = 0
    elif lista[x] % 3 == 0 and lista[x] != 3:
            lista[x] = 0
    elif lista[x] % 5 == 0 and lista[x] != 5:
            lista[x] = 0
    elif lista[x] % 5 == 0 and lista[x] != 5:
            lista[x] = 0
    elif lista[x] % 7 == 0 and lista[x] != 7:
            lista[x] = 0
print(lista)


# In[ ]:




