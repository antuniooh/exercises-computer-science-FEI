#!/usr/bin/env python
# coding: utf-8

# In[4]:


matriz=[]
num = 0
m = []
matriz02 =[]

for num_linha in range(5):
    linha=[]
    for num_coluna in range(4):
        num = int(input("Digite o valor:"))
        linha.append(num)
    matriz.append(linha)
print("")

for linha in range(len(matriz)):
    for coluna in range (len(matriz[linha])):
            m.append(matriz[linha][coluna])
            m.sort()

matriz02.append(m[0:4])
matriz02.append(m[4:8])
matriz02.append(m[8:12])
matriz02.append(m[12:16])
matriz02.append(m[16:20])

for linha in range(len(matriz02)):
    for coluna in range(len(matriz02[linha])):
        print("%2d" % matriz02[linha][coluna], end=" ")
    print()

print("")



# In[ ]:




