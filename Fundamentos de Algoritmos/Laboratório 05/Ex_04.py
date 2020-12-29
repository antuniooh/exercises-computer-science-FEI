#!/usr/bin/env python
# coding: utf-8

# In[6]:


numeros =[]
impar =[]
par = []

while True:
    num = input("Digite um número: ")
    
    if num == "":
        break
    
    else:
        num = int(num)
        numeros.append(num)
        if num % 2 == 0:
            par.append(num)
        elif num % 2 == 1:
            impar.append(num)
            
print("Lista de Todos os numeros:", numeros)
print("Lista de Todos os numeros pares:", par)
print("Lista de Todos os numeros impares:", impar)


# In[ ]:




