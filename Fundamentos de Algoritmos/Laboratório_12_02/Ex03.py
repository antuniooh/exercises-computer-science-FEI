#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      unifansilva
#
# Created:     08/05/2019
# Copyright:   (c) unifansilva 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter.ttk import Checkbutton
from tkinter import messagebox
#importar a biblioteca "os" para poder apagar o arquivo e manipular outras funções
import os
#importar a biblioteca para manipular as linhas dentro do arquvio
from io import StringIO

#cria a variavel janela
janela = Tk()

#atribui um tiulo a variavel janela
janela.title("Aluguel de carros")

#atribui o tamanho da janela
janela.geometry('600x600')

menu = Menu(janela)

#opcÃ§oes de cadastro - labels
Titulo = Label(janela, text="Cadastro de VeÃ­culos", font=("Arial",22))
Titulo.place(x =200, y=10, anchor=CENTER)

marca_l = Label(janela, text="Marca", font=("Arial",12))
marca_l.place(x =100, y=50, anchor=CENTER)

modelo_l = Label(janela, text="Modelo", font=("Arial",12))
modelo_l.place(x=100, y=80, anchor=CENTER)

ano_l = Label(janela, text="Ano de FabricaÃ§Ã£o", font=("Arial",12))
ano_l.place(x=100, y=110, anchor=CENTER)

placa_l = Label(janela, text="Placa", font=("Arial",12))
placa_l.place(x=100, y=140, anchor=CENTER)

km_l = Label(janela, text="Kilometragem", font=("Arial",12))
km_l.place(x=100, y=170, anchor=CENTER)

ar_l = Label(janela, text="Ar Condicionado", font=("Arial",12))
ar_l.place(x=100, y=200, anchor=CENTER)

direcao_l = Label(janela, text="DireÃ§Ã£o HidrÃ¡ulica", font=("Arial",12))
direcao_l.place(x=100, y=230, anchor=CENTER)

radio_l = Label(janela, text="RÃ¡dio", font=("Arial",12))
radio_l.place(x=100, y=260, anchor=CENTER)

airbag_l = Label(janela, text="Airbag", font=("Arial",12))
airbag_l.place(x=100, y=290, anchor=CENTER)

#entradas
marca_t = Entry(janela, width=14, font=("Arial",12))
marca_t.place(x = 250, y = 50, anchor=CENTER)

modelo_t = Entry(janela, width=14, font=("Arial",12))
modelo_t.place(x = 250, y = 80, anchor=CENTER)

ano_t = Entry(janela, width=14, font=("Arial",12))
ano_t.place(x = 250, y = 110, anchor=CENTER)

placa_t = Entry(janela, width=14, font=("Arial",12))
placa_t.place(x = 250, y = 140, anchor=CENTER)

km_t = Entry(janela, width=14, font=("Arial",12))
km_t.place(x = 250, y = 170, anchor=CENTER)

ar_state = BooleanVar()
ar_state.set(False)
ar_c = Checkbutton(janela, text="Possui", var = ar_state)
ar_c.place(x = 250, y = 200,anchor=CENTER)

dir_state = BooleanVar()
dir_state.set(False)
dir_c = Checkbutton(janela, text="Possui", var = dir_state)
dir_c.place(x = 250, y = 230,anchor=CENTER)

radio_state = BooleanVar()
radio_state.set(False)
radio_c = Checkbutton(janela, text="Possui", var = radio_state)
radio_c.place(x = 250, y = 260,anchor=CENTER)

air_state = BooleanVar()
air_state.set(False)
air_c = Checkbutton(janela, text="Possui", var = air_state)
air_c.place(x = 250, y = 290,anchor=CENTER)

def salvar():
    arquivo = open(placa_t.get() + ".txt","w")

    arquivo.write("%s \n" % marca_t.get())
    arquivo.write("%s \n" % modelo_t.get())
    arquivo.write("%d \n" % int(ano_t.get()))
    arquivo.write("%s \n" % placa_t.get())
    arquivo.write("%s \n" % km_t.get())
    arquivo.write("%s \n" % ar_state.get())
    arquivo.write("%s \n" % dir_state.get())
    arquivo.write("%s \n" % radio_state.get())
    arquivo.write("%s \n" % air_state.get())

    res = messagebox.showinfo("Resultado","Criado com sucesso")
    print(res)

    arquivo.close()

#button
enviar = Button(janela, text="Enviar", command=salvar)
enviar.place(x =200, y = 320, anchor=CENTER)
def click():
    new_janela = Tk()
    new_janela.title("Pesquisa de VeÃ­culos")
    new_janela.geometry('500x500')
    #definiÃ§Ã£o dos itens q vÃ£o nela
    placa_l = Label(new_janela, text="Placa do veículo", font=("Arial",12))
    placa_l.place(x=250, y=50, anchor=CENTER)

    placa_t = Entry(new_janela, width=14, font=("Arial",12))
    placa_t.place(x = 250, y = 100, anchor=CENTER)

    result = Label(new_janela, text="", font=("Arial",12))
    result.place(x=250, y=200, anchor=CENTER)

    def buscar():
        #solicitação para o usuário das variaveis necessárias
        placa = placa_t.get()
        try:
            arquivo = open(str(placa) + ".txt", 'r+')
        except OSError:
            res = messagebox.showinfo("Resultado","Arquivo não encontrado")
            print(res)

        c = arquivo.readlines()

        marca = (c[0].rstrip(" \n"))
        modelo = (c[1].rstrip(" \n"))
        ano = (c[2].rstrip(" \n"))
        placa = (c[3].rstrip(" \n"))
        km = (c[4].rstrip(" \n"))
        ar = (c[5].rstrip(" \n"))
        dire = (c[6].rstrip(" \n"))
        radio = (c[7].rstrip(" \n"))
        air = (c[8].rstrip(" \n"))

        resultado = ("Marca do carro: " + marca + "\n"
        +"Modelo do carro: " + modelo + "\n"
        + "Ano do carro: " + ano + "\n"
        + "Placa do carro: " + placa + "\n"
        + "Quilometragem: " + km + "\n"
        + "Possui ar condicionado: " + ar + "\n"
        + "Possui direção hidraúlica: " + dire + "\n"
        + "Possui radio: " + radio + "\n"
        + "Possui air bag: " + air + "\n")

        result['text'] = resultado

        arquivo.close()

    def limpeza():
        result['text'] =""

    #button
    enviar = Button(new_janela, text="Enviar", command=buscar)
    enviar.place(x =250, y = 300, anchor=CENTER)

    limpar = Button(new_janela, text="Limpar", command=limpeza)
    limpar.place(x =200, y = 300, anchor=CENTER)

    new_janela.mainloop()

#cria menu
new_item = Menu(menu)
new_item = Menu(menu, tearoff=0)

menu.add_cascade(label="OpÃ§Ãµes", menu=new_item)

new_item.add_command(label="Pesquisa",command=click)



janela.config(menu=menu)
#chama a funÃ§Ã£o mainloop,para manter sempre aberta
janela.mainloop()



