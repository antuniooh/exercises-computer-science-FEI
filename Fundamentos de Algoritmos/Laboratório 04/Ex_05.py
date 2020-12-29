#!/usr/bin/env python
# coding: utf-8

# In[18]:


letra = input("Digite a coluna da posição: ")
num = int(input("Digite a linha da posição: "))

if letra == "a" and num == 1 or letra =="c" and num == 1 or letra =="e" and num == 1 or letra =="g" and num == 1:
    print("A posição digitada é de um quadrado preto")
elif letra == "a" and num % 2 == 1 or letra =="c" and num % 2 == 1 or letra =="e" and num % 2 == 1 or letra =="g" and num % 2 == 1:
    print("A posição digitada é de um quadrado preto")
elif letra == "a" and num % 2 == 0 or letra =="c" and num % 2 == 0 or letra =="e" and num % 2 == 0 or letra =="g" and num % 2 == 0:
    print("A posição digitada é de um quadrado branco")
elif letra == "b" and num == 1 or letra =="d" and num == 1 or letra =="f" and num == 1 or letra =="h" and num == 1:
    print("A posição digitada é de um quadrado branco")
elif letra == "b" and num % 2 == 1 or letra =="d" and num % 2 == 1 or letra =="f" and num % 2 == 1 or letra =="h" and num % 2 == 1:
    print("A posição digitada é de um quadrado branco")
elif letra == "b" and num % 2 == 0 or letra =="d" and num % 2 == 0 or letra =="f" and num % 2 == 0 or letra =="h" and num % 2 == 0:
    print("A posição digitada é de um quadrado preto")
else:
    print("O valor inserido não se encontra em um tabuleiro de xadrez")


# In[ ]:





# In[ ]:




