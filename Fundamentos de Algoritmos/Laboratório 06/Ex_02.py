#!/usr/bin/env python
# coding: utf-8

# In[4]:


sexo_l = []
cor_olho_l =[]
cor_cabelo_l= []
idade_l =[]

def ler(sexo, cor_olhos, cor_cabelos, idade):
    sexo_l.append(sexo)
    cor_olho_l.append(cor_olhos)
    cor_cabelo_l.append(cor_cabelos)
    idade_l.append(str(idade))


def media(idade_l, cor_olho_l, cor_cabelo_l):
    pessoas = 0
    idade = 0
    for x in range(len(cor_olho_l)):
        if cor_olho_l[x] == "Castanhos" and cor_cabelo_l[x] == "Pretos":
            idade += int(idade_l[x])
            pessoas += 1
    if pessoas == 0:
        print("Não há pessoas com essas caracteristicas")
    else:       
        print("A média da idade das pessoas de cabelos castanhos e olhos pretos é: ", idade/pessoas)
        
def idadeT(idade_l):
    maior = 0
    for x in range(len(idade_l)):
        if int(idade_l[x]) > maior: 
            idadeInt = int(idade_l[x])
            maior = idadeInt
    print("A maior da idade das pessoas é: ", maior)


def mulher_jovem(sexo_l,cor_olho_l, cor_cabelo_l, idade_l):
    pessoas = 0
    for x in range(len(sexo_l)):
        if sexo_l[x] == "F" and cor_cabelo_l[x] == "Louros" and cor_olho_l[x] =="Azuis":
            if int(idade_l[x]) > 18 and int(idade_l[x]) < 36:
                 pessoas += 1
            
    print("A quantidade de mulheres é: ", pessoas)
    
    
    
def main():
    for x in range(1,6):
        sexo = input("Digite o sexo: M ou F ")
        cor_olhos = input("Digite a cor dos olhos: ")
        cor_cabelos = input("Digite a cor dos cabelos: ")
        idade = int(input("Digite a idade: "))
        ler(sexo, cor_olhos, cor_cabelos, idade)
    print("")
    media(idade_l, cor_olho_l, cor_cabelo_l) 
    mulher_jovem(sexo_l, cor_olho_l, cor_cabelo_l,idade_l)
    idadeT(idade_l)
main()


# In[ ]:





# In[ ]:




