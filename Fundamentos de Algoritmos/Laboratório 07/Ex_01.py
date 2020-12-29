#!/usr/bin/env python
# coding: utf-8

# In[3]:


MINMAX = 0
MIN = 100
indice =0

from random import uniform

matriz=[]

for num_linha in range(5):
    linha=[]
    for num_coluna in range(7):
        linha.append(uniform(0,99))
    matriz.append(linha)

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print("%2d" % matriz[linha][coluna], end=" ")
    print()

print("")

for linha in range(len(matriz)):
    for coluna in range (len(matriz[linha])):
        if matriz[linha][coluna] <= MIN:
            MIN = matriz[linha][coluna]
            indice = matriz[linha]
print("Menor Valor da Linha: ", MIN)

for x in indice:
    if x >= MINMAX:
        MINMAX = x
print("Maior Valor da Linha:", MINMAX)
            
print()


# In[ ]:




