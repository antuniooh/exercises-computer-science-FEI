#!/usr/bin/env python
# coding: utf-8

# In[2]:


#função reversa
def procuraReversa(dicionario, v):
   keys = []      
   for chave, valor in dicionario.items():
       if valor == v:
           keys.append(chave)
   return keys

#função princiapl
def main ():
   
   d = {
       1: "a",
       2: "n",
       3: "a",
       4: "j",
       5: "u",
       6: "l",
       7: "i",
       8: "a"
       }
   print(procuraReversa(d, "a"))
 

main()


# In[ ]:




