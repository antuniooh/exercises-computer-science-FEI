#!/usr/bin/env python
# coding: utf-8

# In[26]:


#cria a string e tira os espaços, poe tudo em minusculo
texto = input("Digite o texto: ")
texto = texto.lower()
texto = texto.replace(" ","")

#cria um dicionario com todas as letras do alfabeto
dic = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d":0,
    "e":0,
    "f":0,
    "g":0,
    "h":0,
    "i":0,
    "j":0,
    "k":0,
    "l":0,
    "m":0,
    "n":0,
    "o":0,
    "p":0,
    "q":0,
    "r":0,
    "s":0,
    "t":0,
    "u":0,
    "v":0,
    "w":0,
    "x":0,
    "y":0,
    "z":0
}
#função comparação
for x in range(len(texto)):
    for chave, valor in dic.items():
        #caso a chave do dicionario seja igual a letra da string, soma 1
        if chave == str(texto[x]):
            dic[chave] +=1


#função soma de caracteres
total = 0
for chave,valor in dic.items():
    #caso o valor da chave seja maior que zero, soma 1
    if dic[chave] > 0:
        total += 1
print("O Total de caracteres únicos é: ", total)


# In[ ]:




