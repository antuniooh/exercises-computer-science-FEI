#!/usr/bin/env python
# coding: utf-8

# In[31]:


from random import randint

#dicionario vezes
valores = {
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0
        }
    
#função lançamento de dados
def dados():
    x  = randint(1, 6)
    y  = randint (1,6)  
    valores[x+y] +=1
            
def imprimir(): 
    for chave, valor in valores.items():
        print("%2s = %4s: %2s%%"% (chave, valor, ((valor*100)/10000)))


#função principal
def main():
    for a in range (1, 1001):
        dados()
    
    imprimir()
    

main()


# In[ ]:




