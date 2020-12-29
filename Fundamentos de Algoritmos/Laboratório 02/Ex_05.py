
# coding: utf-8

# In[8]:


from math import *

x = float(input("Digite o valor do lado A, sendo esse a hipotenusa: "))
y = float(input("Digite o valor do lado B: "))
z = float(input("Digite o valor do lado C: "))

#anular variaveis nulas
if x == 0:
    print("O valor é nulo, não é possivel realizar o calculo")
if y == 0:
    print("O valor é nulo, não é possivel realizar o calculo")
if z == 0:
    print("O valor é nulo, não é possivel realizar o calculo")

if x ** 2 == y ** 2 + z **2:
    print("O triângulo é retângulo")
    
if x ** 2 > y ** 2 + z **2:
    print("O triângulo é obtusângulo")
    
if x ** 2 < y ** 2 + z **2:
    print("O triângulo é acutângulo")
    
    


# In[ ]:


2

