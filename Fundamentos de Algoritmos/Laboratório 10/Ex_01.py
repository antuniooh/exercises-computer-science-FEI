#!/usr/bin/env python
# coding: utf-8

# In[5]:


s = input("Digite o texto: ")

s = s.lower() #tudo em minusculas
s = s.replace(" ","") # tirar os espaços

s_n = s[::-1] #string invertida

#inverter com laço
#for x in range(1, len(s) + 1):
#    s_n += s[-x]
    
if s == s_n:
    print("É Palíndromo")
else:
    print("Não é Palíndromo ")


# In[ ]:




