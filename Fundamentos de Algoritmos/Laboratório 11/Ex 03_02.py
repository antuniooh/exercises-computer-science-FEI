#!/usr/bin/env python
# coding: utf-8

# In[4]:


def main():
    letras = {}
    texto = input("Insira um texto qualquer: ")
    
    for x in texto:
        letras[x] = 0
    
    print(letras)
    print("quantidade de letras ", len(letras))

main()


# In[ ]:




