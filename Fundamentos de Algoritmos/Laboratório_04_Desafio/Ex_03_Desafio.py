#!/usr/bin/env python
# coding: utf-8

# In[3]:


clas = float(input("Digite o valor da classificação do funcionário: "))
Aumento = 0.0

if clas != 0.0 and clas != 0.4 and clas != 0.6 and clas < 0.6:
    print("A classificação não está dentro do valor")
    Status = "Indefinido"
    Aumento = 0.0
else:
    if clas == 0.0:
        Status = "Inaceitável"
        Aumento = 0.0 * 2400
    elif clas == 0.4:
        Status = "Aceitável"
        Aumento = 0.4 * 2400
    else:
        Status = "Excelente"
        Aumento = clas * 2400

        
        
print(clas,"/",Status,"/", Aumento)


# In[ ]:





# In[ ]:




