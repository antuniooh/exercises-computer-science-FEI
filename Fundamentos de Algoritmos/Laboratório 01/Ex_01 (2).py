
# coding: utf-8

# In[1]:


print("Primeiro Programa em Python")


# In[ ]:


Nome = input("Insira seu nome: ")
print(Nome)


# In[ ]:


n1 = float(input("Insira o Primeiro Valor: "))
n2 = float(input("Insira o Segundo Valor: "))
n3 = n1 + n2
print(n3)


# In[ ]:


raio = float(input("Insira o Valor do Raio: "))
area = (3.14159 * (raio ** 2))
print(area)


# In[ ]:


f = float(input("Insira o Valor da Temperatura em Fahreint: "))
Celsiu = (5 * (f-32) / 9)
print("A Temperatura é ",Celsiu,"°C")


# In[ ]:


LAB = float(input("Insira a nota de Laboratório: "))
P1 = float(input("Insira a nota da P1: "))
P2 = float(input("Insira a nota da P2: "))
Media = (LAB + 2 * P1 + 3* P2)/6
print(Media)

