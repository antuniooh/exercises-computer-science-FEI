#!/usr/bin/env python
# coding: utf-8

# In[11]:


P1 = input("Telefonou para a vítima?: ")
P2 = input("Esteve no local do crime?: ")
P3 = input("Mora perto da vítima?: ")
P4 = input("Devia para a vítima?: ")
P5 = input("Já trabalhou com a vítima?: ")

i = 0

if P1 == "Sim":
    i+=1
elif P1 =="Não":
    i+=0
else:
    print("Digite 'Sim' ou 'Não'")
    
if P2 == "Sim":
    i+=1
elif P2 =="Não":
    i+=0
else:
    print("2Digite 'Sim' ou 'Não'")
    
if P3 == "Sim":
    i+=1
elif P3 =="Não":
    i+=0
else:
    print("Digite 'Sim' ou 'Não'")
    
if P4 == "Sim":
    i+=1
elif P4 =="Não":
    i+=0
else:
    print("Digite 'Sim' ou 'Não'")
    
if P5 == "Sim":
    i+=1
elif P5 =="Não":
    i+=0
else:
    print("Digite 'Sim' ou 'Não'")
    
    
if i == 2:
    print("Suspeita")

elif i > 2 and i <= 4:
    print("Cúmplice")
    
elif i == 5:
    print("Culpada")
    
else:
    print("Inocente")

    


# In[ ]:





# In[ ]:




