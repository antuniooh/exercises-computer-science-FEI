#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *

#cria a variavel janela
janela = Tk()

#atribui um tiulo a variavel janela
janela.title("Soma")

#atribui o tamanho da janela
janela.geometry('600x300')

#cria os rotulos (label) na janela desejada, atribui seu texto e configura-o
rotulo1 = Label(janela, text ="Digite o primeiro número: ", font=("Arial ", 12))
rotulo2 = Label(janela, text ="Digite o segundo número: ", font=("Arial ", 12))
result = Label(janela, text ="Resultado:  ", font=("Arial", 12))

#configura o local onde as labels vao aparecer
#sua referencia é o centro
rotulo1.place(x=200, y=100, anchor=CENTER)
rotulo2.place(x=200, y=140, anchor=CENTER)
result.place(x=200, y=180, anchor=CENTER)


#cria as entradas de texto
entrada1 = Entry(janela, width=14, font=("Arial", 12))
entrada1.place(x=400, y=100, anchor=CENTER)
entrada2 = Entry(janela, width=14, font=("Arial", 12))
entrada2.place(x=400, y=140, anchor=CENTER)
saida = Entry(janela, width=14, font=("Arial", 12))
saida.place(x=400, y=180, anchor=CENTER)

#definição da função clique do botao
def soma():
    valor1 = entrada1.get()
    valor2 = entrada2.get()
    resultado = saida.get()
  
    soma = int(valor1) + int(valor2)
    if resultado !="":
        saida.delete(0,END)
        
        saida.insert(0,str(soma))
    else:
        saida.insert(0,str(soma))
    

#cria os botoes na janela
calcula = Button(janela, text="Soma!", command=soma)


#configura onde ele vai aparecer
calcula.place(x=200, y=220, anchor=CENTER)


#chama a função mainloop,para manter sempre aberta
janela.mainloop()


# In[ ]:




