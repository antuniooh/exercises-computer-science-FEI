#!/usr/bin/env python
# coding: utf-8

# In[6]:


from tkinter import *

#cria a variavel janela
janela = Tk()

#atribui um tiulo a variavel janela
janela.title("Algoritmos")

#atribui o tamanho da janela
janela.geometry('400x400')

#cria o rotulo (label) na janela desejada, atribui seu texto e configura-o
rotulo = Label(janela, text ="Primeira aplicação gráfica no Python!", font=("Arial Bold", 14))

#configura o local onde esse label vai aparecer
#sua referencia é o centro
rotulo.place(x=200, y=100, anchor=CENTER)

#cria uma entrada de texto
entrada = Entry(janela, width=14, font=("Arial Bold", 14))
entrada.place(x=200, y=50, anchor=CENTER)

#definição da função clique do botao
def clique():
    resposta = entrada.get()
    rotulo['text'] = resposta

#cria o botao na janela
botao = Button(janela, text="Clique aqui!", command=clique)

#configura onde ele vai aparecer
botao.place(x=200, y=200, anchor=CENTER)

#chama a função mainloop,para manter sempre aberta
janela.mainloop()


# In[ ]:




