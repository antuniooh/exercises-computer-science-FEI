#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *
from tkinter import scrolledtext
import os

#janela
janela = Tk()
janela.title("Discurso de Ódio - Software")
janela.geometry("700x500")

#labels
palavraS = Label(janela, text="Palavra suspeita: ", font=("Arial",12))
palavraS.place(x=100, y =50, anchor=CENTER)

frequenciaL = Label(janela, text="Frequência: ", font=("Arial",12))
frequenciaL.place(x=100, y =70, anchor=CENTER)

#entradas
palavraSus = Entry(janela, width=14, font=("Arial",12))
palavraSus.place(x=250, y =50, anchor=CENTER)
frequenciaE = Entry(janela, width=14, font=("Arial",12))
frequenciaE.place(x=250, y =70, anchor=CENTER)
resultado = scrolledtext.ScrolledText(janela, width=80, height=15)
resultado.place(x=350, y= 250, anchor=CENTER)

def pesquisa():
    p = palavraSus.get()
    p = p.lower()
    f = 0

    #abrir o arquvio
    arquivo = open("p2-chat.txt","r")

    #armazena-se as linhas em uma string
    #descobre a quantidade de linhas

    lista = []
    lista2 =[]
    for linha in arquivo.readlines():
        lista2.append(linha)
        palavras = linha.replace("\t"," ").replace(","," ").replace("!"," ").replace("?"," ").replace("\n"," ").replace("."," ").lower().strip().split()
        lista.append(palavras)
    print(lista)


    for x in range(len(lista)):
        for y in range(len(lista[x])):
            if lista[x][y] == p:
                f +=1
                resposta = lista2[x] + "\n"
                resultado.insert(END,resposta)


    #na frequencia entry, confere se não há nada escrito
    if frequenciaE !="":
        frequenciaE.delete(0,END)
        frequenciaE.insert(0,f)
    else:
        frequenciaE.insert(0,f)

    arquivo.close()

#buttons
pesquisar = Button(janela, text="Pesquisar",command=pesquisa)
pesquisar.place(x=350, y = 50, anchor=CENTER)


janela.mainloop()


# In[ ]:





# In[ ]:




