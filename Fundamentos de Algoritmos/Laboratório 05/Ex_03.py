#!/usr/bin/env python
# coding: utf-8

# In[36]:


carros = ["Corolla","Civic","Vectra","Duster", "Punto"]
consumo = [10,20,30,40,50]
menor = 1

#for x in range(0,6):
#    car = input("Digite um carro: ")
#    cons = int(input("Digit o consumo de litro por KM: "))
#    carros.append(car)
#    consumo.append(cons)


for x in range (len(consumo)):
    if consumo[x] <= menor:
        menor = consumo[x]
    
print ("Carro mais economico:", carros[menor - 1])
print("")
print("Consumo de cada Carro: ")
print("")
print(carros[0], "Consumo R$: ", (consumo [0] * 1000)/4.09)
print(carros[1], "Consumo R$: ", (consumo [1] * 1000)/4.09)
print(carros[2], "Consumo R$: ", (consumo [2] * 1000)/4.09)
print(carros[3], "Consumo R$: ", (consumo [3] * 1000)/4.09)
print(carros[4], "Consumo R$: ", (consumo [4] * 1000)/4.09)


# In[ ]:





# In[ ]:




