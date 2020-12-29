#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randint

matriz=[]

for num_linha in range(10):
    linha=[]
    for num_coluna in range(15):
        linha.append(randint(0,99))
    matriz.append(linha)

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print("%2d" % matriz[linha][coluna], end=" ")
    print()

print("")
print("Transversal:")

for linha in range(15):
    for coluna in range(10):
        print("%2d" % matriz[coluna][linha], end=" ")
    print()


# In[ ]:




