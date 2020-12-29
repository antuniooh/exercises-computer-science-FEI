#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      unifansilva
#
# Created:     09/05/2019
# Copyright:   (c) unifansilva 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter import messagebox

#cria a variavel janela
janela = Tk()

#atribui um tiulo a variavel janela
janela.title("CronÃ´metro de Pomodoro")

#atribui o tamanho da janela
janela.geometry('600x300')

menu = Menu(janela)

#opcÃ§oes de cadastro - labels
Titulo = Label(janela, text="Tarefa:", font=("Arial",14))
Titulo.place(x =300, y=20, anchor=CENTER)

relogio = Label(janela, text ="25:00", font=("Arial ", 14), foreground='blue')
relogio.place(x=300, y=110, anchor=CENTER)

#entradas
tarefa = Entry(janela, width=30, font=("Arial",12))
tarefa.place(x = 300, y = 50, anchor=CENTER)

tarefas = ""

#minutos e segundos
m = 5
s = 0

def pausar():
    global m,s,tarefas
    res = messagebox.showinfo('Tempo Esgotado','Fim da tarefa: '+ tarefa.get()+"\n" + str(m)+":"+str(s))
    tarefas += tarefa.get() + "/ Tempo Usado: " + str(27 - m) +":"+ str(62 - s) + "\n"
    #para parar o loop
    relogio['text'] = "25:00"
    if relogio['text'] == "25:00":
        m = -2
        s = -2




def iniciar():
    global m,s
    m = 25
    s = 0
    def tempo():
        global m,s,tarefas
        relogio['text'] = str(m) + ":" + str(s)
        if m >= 0 :
            s-=1
            if s == -1:
                m-=1
                s = 59
                if m ==-1:
                    tarefas += tarefa.get() + "/ Tempo Usado: 25:0 \n"
                    res = messagebox.showinfo('Tempo Esgotado','Fim da tarefa: '+ tarefa.get())
                    relogio['text'] = "25:00"
        else:
            relogio['text'] = "25:00"

        janela.after(10,tempo)
    tempo()


print(tarefas)

#button
inicio = Button(janela, text="Inicio", command=iniciar)
inicio.place(x =300, y = 80, anchor=CENTER)

pause = Button(janela, text="Pausar", command=pausar)
pause.place(x =300, y = 140, anchor=CENTER)

def click():
    global tarefas
    new_janela = Tk()
    new_janela.title("Tarefas Completadas")
    new_janela.geometry('600x300')
    #definiÃ§Ã£o dos itens q vÃ£o nela
    lista = Label(new_janela, text="AAAAA")
    lista.place(x = 300, y = 50)
    lista['text'] = str(tarefas)
    new_janela.mainloop()

#cria menu
new_item = Menu(menu)
new_item = Menu(menu, tearoff=0)

menu.add_cascade(label="Tarefas Completadas", command=click)
janela.config(menu=menu)


janela.mainloop()