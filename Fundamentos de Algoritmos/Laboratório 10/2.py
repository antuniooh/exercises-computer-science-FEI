#!/usr/bin/env python
# coding: utf-8

# In[ ]:


novo= open("Python.txt","r")
lista=[]
tam=[]
maiores = []

for linha in novo.readlines():
  separado=linha.replace(".","").replace(",","").strip().split()
  lista.append(separado)
novo.close()

for a in range(len(lista)):
  for b in range(len(lista[a])):
    tamanho=len(lista[a][b])
    tam.append(tamanho)
print(max(tam)) 

for a in range(len(lista)):
  for b in range(len(lista[a])):  
    if len(lista[a][b]) == max(tam):
      if lista[a][b] not in maiores:
        maiores.append(lista[a][b])

print(maiores) 

