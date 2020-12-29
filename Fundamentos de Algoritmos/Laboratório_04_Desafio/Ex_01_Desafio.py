#!/usr/bin/env python
# coding: utf-8

# In[3]:


ano = int(input("Digite o ano de nascimento: "))

if ano <=0:
    print("O ano não é valido")
    

if ano % 12 == 8:
    print("Dragao")
elif ano % 12 == 9:
    print("Cobra")
elif ano % 12 == 10:
    print("Cavalo")
elif ano % 12 == 11:
    print("Carneiro")
elif ano % 12 == 0:
    print("Macaco")
elif ano % 12 == 1:
    print("Galo")
elif ano % 12 == 2:
    print("Cachorro")
elif ano % 12 == 3:
    print("Porco")
elif ano % 12 == 4:
    print("Rato")
elif ano % 12 == 5:
    print("Boi")
elif ano % 12 == 6:
    print("Tigre")
elif ano % 12 == 7:
    print("Lebre")
    


# In[ ]:




