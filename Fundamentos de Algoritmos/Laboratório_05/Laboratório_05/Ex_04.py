#!/usr/bin/env python
# coding: utf-8

# In[1]:


numeros =[]
negativos =[]
positivos = []
nulos = []

while True:
    num = input("Digite um número: ")
    
    if num == "":
        break
    
    else:
        num = int(num)
        numeros.append(num)
        if num > 0:
            positivos.append(num)
        elif num < 0:
            negativos.append(num)
        else:
            nulos.append(num)
            
print("Lista de Todos os numeros:", numeros)
print("Lista de Todos os numeros positivos:", positivos)
print("Lista de Todos os numeros negativos:", negativos)
print("Lista de Todos os numeros nulos:", nulos)


# In[ ]:




