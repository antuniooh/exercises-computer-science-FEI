#!/usr/bin/env python
# coding: utf-8

# In[9]:


mes = input("Digite o mês: ")
dia = int(input("Digite o dia: "))

if mes =="Janeiro":
    mes = 1
    
elif mes =="Fevereiro":
    mes = 2
    
elif mes =="Março":
    mes = 3
    
elif mes =="Abril":
    mes = 4
    
elif mes =="Maio":
    mes = 5
    
elif mes =="Junho":
    mes = 6
    
elif mes =="Julho":
    mes = 7
    
elif mes =="Agosto":
    mes = 8
    
elif mes =="Setembro":
    mes = 9
    
elif mes =="Outubro":
    mes = 10
    
elif mes =="Novembro":
    mes = 11
    
elif mes =="Dezembro":
    mes = 12
    
else:
    print("O mês digitado não existe")
    
if dia <= 0 or dia > 31:
    print("O dia digitado não existe")    
    
#outono
if mes == 3 and dia >= 20:
    print("A estação na data digitada é Outono")
elif mes == 4 or mes == 5:
    print("A estação na data digitada é Outono")
elif mes == 6 and dia < 21:
    print("A estação na data digitada é Outono")
    
#inverno
if mes == 6 and dia >= 21:
    print("A estação na data digitada é Inverno")
elif mes == 7 or mes == 8:
    print("A estação na data digitada é Inverno")
elif mes == 9 and dia < 22:
    print("A estação na data digitada é Inverno")

#primavera
if mes == 9 and dia >= 22:
    print("A estação na data digitada é Primavera")
elif mes == 10 or mes == 11:
    print("A estação na data digitada é Primavera")
elif mes == 12 and dia < 21:
    print("A estação na data digitada é Primavera")

#verão
if mes == 12 and dia >=21:
    print("A estação na data digitada é Verão")
elif mes == 1 or mes == 2:
    print("A estação na data digitada é Verão")
elif mes == 3 and dia < 20:
    print("A estação na data digitada é Verão")



# In[ ]:




