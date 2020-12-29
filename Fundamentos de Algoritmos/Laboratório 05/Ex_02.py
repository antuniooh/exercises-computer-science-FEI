#!/usr/bin/env python
# coding: utf-8

# In[5]:


par = []
impar = []
numeros = []

for x in range (1,21):
    num = int(input("Digite um numero: "))
    numeros.insert(0,num)
    if num % 2 == 0:
        par.insert(0,num)
    elif num % 2 ==1:
        impar.insert(0,num)
    
    
print("Lista de todos os números: ",numeros)
print("Lista de todos os impares: ",impar)
print("Lista de todos os pares: ",par)


# In[ ]:





# In[ ]:




