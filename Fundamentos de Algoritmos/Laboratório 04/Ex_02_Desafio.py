#!/usr/bin/env python
# coding: utf-8

# In[3]:


dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))
ano = int(input("Digite o ano: "))

#bissexto status
if (ano % 400 == 0) or ((ano % 4 == 0) and (ano % 100 !=0)):
    status = "bissexto"
else:
    status = "não bissexto"

# validar mes
if mes <= 0 or mes > 12:
    print("O mes digitado não existe")
    

#validar ano
if ano <= 0:
    print("O ano digitado não existe")
    


#dia
if dia <= 0 or dia > 31:
    print("O dia digitado não existe")
#bissexto
elif mes == 2 and status == "bissexto" and dia == 29:
    mes +=1
    dia = 1
elif mes == 2 and status == "não bissexto" and dia == 29:
    print("o ano digitado não é bissexto")
elif mes == 2 and status == "não bissexto" and dia == 28:
    mes +=1
    dia = 1
#mes normal
elif dia == 31 and mes != 12:
    mes +=1
    dia = 1
elif mes == 12 and dia == 31:
    mes = 1
    dia = 1
    ano += 1
else:
    dia +=1

    
print("O dia seguinte é: ", dia, "/",mes,"/",ano, " - ", status)
    



# In[ ]:





# In[ ]:




