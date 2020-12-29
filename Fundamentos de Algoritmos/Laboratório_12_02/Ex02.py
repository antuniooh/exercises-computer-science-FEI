#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from datetime import datetime

#cria a variavel janela
janela = Tk()

#atribui um tiulo a variavel janela
janela.title("Relógio Digital")

#atribui o tamanho da janela
janela.geometry('600x300')

#cria os rotulos (label) na janela desejada, atribui seu texto e configura-o
relogio = Label(janela, text ="", font=("Arial ", 14), foreground='blue')
data = Label(janela, text ="", font=("Arial", 14), foreground='blue')

#configura o local onde as labels vao aparecer
#sua referencia é o centro
relogio.place(x=200, y=100, anchor=CENTER)
data.place(x=200, y=180, anchor=CENTER)


def loop():
    now = datetime.now()
    data_a = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
    data['text'] = data_a
    hora =  str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
    relogio['text'] = hora
    janela.after(1000, loop)

loop()
#chama a função mainloop,para manter sempre aberta
janela.mainloop()



# In[ ]:




