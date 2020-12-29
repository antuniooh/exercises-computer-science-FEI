#!/usr/bin/env python
# coding: utf-8

# In[39]:


arquivo = open("Python.txt", "r", encoding = "utf-8")

lista = ""

#colocar na string lista as seis linhas
for x in range(1,7):
    lista += arquivo.readline()
    lista = lista.strip("\n") # tira a quebra de linha
    lista = lista.replace(","," ")#tira os sinais orotgraficos
    lista = lista.replace("."," ")
    lista = lista.lower()#coloca tudo como minusculos
    
lista = lista.split(" ")# quebra em diversos itens
    
arquivo.close()    
    
tamanho = 0
i = 0

#qual o maior tamanho
for x in range(len(lista)):
    if len(lista[x]) > tamanho:
        tamanho = len(lista[x])
        
#quantas vezes ele aparece e em quais palavras
for x in range(len(lista)):
    if len(lista[x]) == tamanho:
        i += 1
        print("Maiores palavras:", lista[x])
        
print("Maior tamanho de String: ", tamanho," Número de vezes que se repete: ", i)


# In[ ]:




