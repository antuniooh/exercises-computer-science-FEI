
# coding: utf-8

# In[1]:


def aleatoria():
    from random import randrange 
    arquivo = open("palavras.txt","r", encoding="utf-8-sig")
    

    for linha in arquivo.readlines():
        a = linha.replace(",", " ").strip().split()
    
    y = randrange(0,len(a))
    aleatoria = a[y]
    return(aleatoria)
    
aleatoria()

