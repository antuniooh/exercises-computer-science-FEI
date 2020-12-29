#!/usr/bin/env python
# coding: utf-8

# In[10]:


from math import sqrt

a = float(input("Digite o valor de A: "))

if a == 0:
    exit()
    
else:
    b= float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))
    
    delta = (b ** 2) - 4 * a * c
    
    if delta < 0:
        print("A equação não possui raizes reais")
        exit()
    elif delta ==0:
        raiz= (-b)/2 * a
        print("A equação possui apenas uma raiz real: ", raiz)
        
    else:
        raiz1= (-b  + (sqrt(delta) * -1))/2 * a
        raiz2= (-b  + (sqrt(delta) * 1))/2 * a
        print("A equação possui duas raízes: ", raiz1, " ", raiz2 )
        


# In[ ]:




