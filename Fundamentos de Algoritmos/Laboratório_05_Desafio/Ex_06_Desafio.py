#!/usr/bin/env python
# coding: utf-8

# In[10]:


num1 =int(input("Digite o numero: "))
num2 =int(input("Digite o divisor: "))

quo = 0
resto = 0

if num2 == 0:
    print("A divisão não é valida")
elif num2 > num1:
    print("A divisão não é valida")
else: 
    while num1 - num2 >= 0:
        num1 = num1 - num2
        quo +=1
        resto = num1
    
print("O Quociente da divisão é: ", quo)
print("O resto da divisão é: ", resto)


# In[ ]:




