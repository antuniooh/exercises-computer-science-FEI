#!/usr/bin/env python
# coding: utf-8

# In[4]:


from random import randint

matriz=[]
soma = 0

for num_linha in range(12):
    linha=[]
    for num_coluna in range(12):
        linha.append(randint(0,99))
    matriz.append(linha)

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print("%2d" % matriz[linha][coluna], end=" ")
    print()

print("")

opcao = input("Digite a operação desejada: (S ou M): ")

if opcao == "S":
    for linha in range(len(matriz)):
          for coluna in range(0, linha):
                if not coluna == matriz:
                    soma += matriz[linha][coluna]
    print("A soma dos valores abaixo da diagonal é:", soma)

elif opcao == "M":
    for linha in range(len(matriz)):
          for coluna in range(len(matriz[linha])):
                soma += matriz[linha][coluna]
    print("A média é:", soma/66)
    
else:
    print("A opção desejada não é válida")


# In[ ]:




