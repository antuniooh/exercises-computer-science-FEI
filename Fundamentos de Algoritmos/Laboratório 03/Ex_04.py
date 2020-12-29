#!/usr/bin/env python
# coding: utf-8

# In[7]:


litros = int(input("Digite a quantidade de litros vendidos: "))
combustivel = input("Digite o tipo de combustivel: ")

if combustivel == "Álcool":
    if litros <= 20:
        desconto = 0.97 * 2.80
    if litros > 20:
        desconto = 0.95 * 2.80
    
    valor = (litros * desconto)
    print("o valor total é de: R$", valor)
    
elif combustivel == "Gasolina":
    if litros <= 20:
        desconto = 0.96 * 4.20
    if litros > 20:
        desconto = 0.94 * 4.20
        
    valor = (litros * desconto)
    print("o valor total é de: R$", valor)
        


# In[ ]:




