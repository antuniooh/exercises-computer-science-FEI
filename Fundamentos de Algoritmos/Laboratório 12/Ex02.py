#!/usr/bin/env python
# coding: utf-8

# In[56]:


from tkinter import *

#cria a variavel janela
janela = Tk()

#atribui um tiulo a variavel janela
janela.title("Conversão Numérica")

#atribui o tamanho da janela
janela.geometry('600x300')

#cria os rotulos (label) na janela desejada, atribui seu texto e configura-o
rotulo1 = Label(janela, text ="Número decimal: ", font=("Arial ", 12))
result = Label(janela, text ="Resultado:  ", font=("Arial", 12))

#configura o local onde as labels vao aparecer
#sua referencia é o centro
rotulo1.place(x=200, y=100, anchor=CENTER)
result.place(x=200, y=180, anchor=CENTER)


#cria as entradas de texto
entrada1 = Entry(janela, width=14, font=("Arial", 12))
entrada1.place(x=400, y=100, anchor=CENTER)
saida = Entry(janela, width=14, font=("Arial", 12))
saida.place(x=400, y=180, anchor=CENTER)

#definição das funções clique do botao
def binario():
    valor = entrada1.get()
    
    resultado = bin(int(valor))
    
    if resultado !="":
        saida.delete(0,END)
        
        saida.insert(0,str(resultado[2:]))
    else:
        saida.insert(0,str(resultado[2:]))

def hexadecimal():
    valor = entrada1.get()
    
    resultado = hex(int(valor))
    
    if resultado !="":
        saida.delete(0,END)
        
        saida.insert(0,str(resultado[2:]))
    else:
        saida.insert(0,str(resultado[2:]))

def octal():
    valor = entrada1.get()
    
    resultado = oct(int(valor))
    
    if resultado !="":
        saida.delete(0,END)
        
        saida.insert(0,str(resultado[2:]))
    else:
        saida.insert(0,str(resultado[2:]))
    

#cria os botoes na janela
Bina = Button(janela, text="Binário", command=binario)
Hexa = Button(janela, text="Hexadecimal", command=hexadecimal)
Octa = Button(janela, text="Octal", command=octal)


#configura onde ele vai aparecer
Bina.place(x=200, y=140, anchor=CENTER)
Hexa.place(x=280, y=140, anchor=CENTER)
Octa.place(x=360, y=140, anchor=CENTER)


#chama a função mainloop,para manter sempre aberta
janela.mainloop()


# In[ ]:




