#!/usr/bin/env python
# coding: utf-8

# In[26]:


VH = float(input("Digite o valor por hora trabalhada: "))
QH = float(input("Digite a quantidade de horas trabalhadas: "))

Sal_Bruto = VH * QH

FGTS = Sal_Bruto * 0.11

INSS = Sal_Bruto * 0.10

if Sal_Bruto <= 900.00:
    IR = 0
if Sal_Bruto > 900.00 and Sal_Bruto <= 1500.00:
    IR = 5
if Sal_Bruto > 1500.00 and Sal_Bruto <= 2500.0:
    IR = 10
if Sal_Bruto > 2500.0:
    IR = 20
    
Valor_IR = (Sal_Bruto * IR)/100

Sal_Liquido = Sal_Bruto - (INSS + Valor_IR)

print("")
print("Salário Bruto: (%d * %d)    :" % (VH, QH),"R$ ", Sal_Bruto)
print("(-)IR (%d )                 :" % IR, "R$ ",Valor_IR )
print("(-)INSS (10%)               :", "R$ ",INSS)
print("FGTS (11%)                  :", "R$ ",FGTS)
print("____________________________________")
print("Total de descontos          :", "R$ ", INSS + Valor_IR)
print("____________________________________")
print("Salário Liquido             :", "R$ ", Sal_Liquido)


# In[ ]:





# In[ ]:




