#!/usr/bin/env python
# coding: utf-8

# In[10]:


#inserir as strings
texto1 = input("Digite a primeira palavra: ")
texto2 = input("Digite a segunda palavra: ")

#coloca-las em minusculos
texto1 = texto1.lower()
texto2 = texto2.lower()

dic1 = {  }

for x in range(len(texto1)):
    for chave, valor in dic1.items():
        if chave == texto1[x]:
            valor +=1
        else:
            dic1[texto1[x]] = 1
    
for chave, valor in dic1.items():
    print(chave, valor)


# In[ ]:




