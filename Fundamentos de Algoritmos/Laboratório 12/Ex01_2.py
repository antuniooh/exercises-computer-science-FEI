#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importar o thinker
from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.title("Exercicio 1")
janela.geometry('300x600')


#criar entrada
entrada= Entry(janela, width=14, font=('Arial',14))
entrada.place(x=200, y =50, anchor=CENTER)

def avaliar():
    t = entrada.get()
    tamanho = len(t)
    if tamanho > 1 or tamanho < 1:
        res = messagebox.showinfo('Resultado','Tamamho invalido de caracteres')
            print(res)
    else:
        if t == "a" or t == "e" or t == "i" or t == "o" or t == "u":
            res = messagebox.showinfo('Resultado','A letra é vogal')
            print(res)
        elif t == "y" :
            res = messagebox.showinfo('Resultado','A letra as vezes é vogal e as vezes consoante')
            print(res)
        else:
            res = messagebox.showinfo('Resultado','A letra é consoante')
            print(res)

#criar button
botao = Button(janela, text="Resultado", command=avaliar)
botao.place(x =200, y =200, anchor=CENTER)

janela.mainloop()


# In[ ]:




