#!/usr/bin/env python
# coding: utf-8

# In[31]:


from random import randrange
numeros = []

aleatorio = randrange(0,50)
numeros.append(aleatorio)

for x in range(0,5):
    aleatorio = randrange(0,50)

    if aleatorio == numeros[x]:
         continue
    else:
         numeros.append(aleatorio)
            
print(numeros)

        
    


# In[ ]:





# In[ ]:




