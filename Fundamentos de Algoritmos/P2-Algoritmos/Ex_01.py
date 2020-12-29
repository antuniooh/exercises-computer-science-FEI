
# coding: utf-8

# In[1]:


#interface gráfica
from tkinter import *
from tkinter.ttk import Checkbutton
from tkinter import messagebox

janela = Tk()
janela.title("Consumo de Energia Elétrica")
janela.geometry("600x400")

#labels
dataInicial = Label(janela, text="Data Inicial: ", font=("Arial",12))
dataInicial.place(x=100, y=50, anchor=CENTER)
dataFinal = Label(janela, text="Data Final: ", font=("Arial",12))
dataFinal.place(x=100, y=80, anchor=CENTER)
horaInicial = Label(janela, text="Hora Inicial: ", font=("Arial",12))
horaInicial.place(x=380, y=50, anchor=CENTER)
horaFinal = Label(janela, text="Hora Final: ", font=("Arial",12))
horaFinal.place(x=380, y=80, anchor=CENTER)

consumoTotal = Label(janela, text="Consumo Total(kWh) : ", font=("Arial",12))
consumoTotal.place(x=150, y=300, anchor=CENTER)
consumoCalculado = Label(janela, text="Consumo Calculado(kWh): ", font=("Arial",12))
consumoCalculado.place(x=150, y=330, anchor=CENTER)

#Entrys
dataI = Entry(janela, width=14,  font=("Arial",12))
dataI.place(x=220, y=50, anchor=CENTER)
dataF = Entry(janela, width=14,  font=("Arial",12))
dataF.place(x=220, y=80, anchor=CENTER)
horaI = Entry(janela, width=14,  font=("Arial",12))
horaI.place(x=500, y=50, anchor=CENTER)
horaF = Entry(janela, width=14,  font=("Arial",12))
horaF.place(x=500, y=80, anchor=CENTER)

consumoT = Entry(janela, width=14,  font=("Arial",12))
consumoT.place(x=400, y=300, anchor=CENTER)
consumoC = Entry(janela, width=14,  font=("Arial",12))
consumoC.place(x=400, y=330, anchor=CENTER)

#checkButtons
lamp_state = BooleanVar()
lampC = Checkbutton(janela, text="Lâmpada", var= lamp_state)
lampC.place(x= 230, y = 200, anchor=CENTER)
chuv_state = BooleanVar()
chuvC = Checkbutton(janela, text="Chuveiro", var= chuv_state)
chuvC.place(x= 229, y = 230, anchor=CENTER)
tom_state = BooleanVar()
tomC = Checkbutton(janela, text="Tomadas", var= tom_state)
tomC.place(x= 350, y = 200, anchor=CENTER)
ar_state = BooleanVar()
arC = Checkbutton(janela, text="Ar Condicionado", var= ar_state)
arC.place(x= 370, y = 230, anchor=CENTER)
lamp_state.set(False)
chuv_state.set(False)
tom_state.set(False)
ar_state.set(False)

#função
def calcular():
    arquivo = open("consumo.txt","r")
    c = []
    for linha in arquivo.readlines():
        resultado = linha.split()
        c.append(resultado)
    
    #total geral
    total = 0.0
    t = len(c)
    total = (float(c[t - 1][2]) + float(c[t - 1][3]) + float(c[t - 1][4]) + float(c[t - 1][5]))/1000
    
    consumoTotal = consumoT.get()
    if consumoTotal !=" ":
        consumoT.delete(0, END)
        consumoT.insert(0, str(total))
    else:
        consumoT.insert(0, str(total))
    
    #total caluclado
    dI = dataI.get()
    dF = dataF.get()
    hI =  horaI.get()
    hF = horaF.get()
    
    lamp = lamp_state.get() 
    chuv = chuv_state.get() 
    tom = tom_state.get() 
    ar = ar_state.get() 
    
    consumo = 0.0
    for x in range(len(c)):
        if lamp == 1:
            valorI =0.0
            valorF =0.0
            if c[x][0] == dI and c[x][1] == hI:
                valorI = float(c[x][2])
            if c[x][0] == dF and c[x][1] == hF:
                valorF = float(c[x][2])
            consumo += valorF-valorI
            
        if chuv == 1:
            valorI =0.0
            valorF =0.0
            if c[x][0] == dI and c[x][1] == hI:
                valorI = float(c[x][3])
            if c[x][0] == dF and c[x][1] == hF:
                valorF = float(c[x][3])
            consumo += valorF-valorI
        
        if tom == 1:
            valorI =0.0
            valorF =0.0
            if c[x][0] == dI and c[x][1] == hI:
                valorI = float(c[x][4])
            if c[x][0] == dF and c[x][1] == hF:
                valorF = float(c[x][4])
            consumo += valorF-valorI
            
        if ar == 1:
            valorI =0.0
            valorF =0.0
            if c[x][0] == dI and c[x][1] == hI:
                valorI = float(c[x][5])
            if c[x][0] == dF and c[x][1] == hF:
                valorF = float(c[x][5])
            consumo += valorF-valorI
       
            
    
    consumo = consumo/1000  
    print(consumo)
    consumoCalcul = consumoC.get()
    if consumoCalcul !=" ":
        consumoC.delete(0,END)
        consumoC.insert(0, str(consumo))
    else:
        consumoC.insert(0, str(total))
    
        
    
def limpar():
    dataI.delete(0,END)
    dataF.delete(0,END)
    horaI.delete(0,END)
    horaF.delete(0,END)
    consumoT.delete(0,END)
    consumoC.delete(0,END)
    lamp_state.set(False)
    chuv_state.set(False)
    tom_state.set(False)
    ar_state.set(False)
    
def aluno():
    res = messagebox.showinfo('P2  - Algoritmos', "Antonio Gustavo Muniz (22.119.001 - 0)")
    print(res)
    
#buttons
calcularB = Button(janela, text="Calcular", command=calcular)
calcularB.place(x= 200, y = 150, anchor=CENTER)
limparB = Button(janela, text="Limpar", command=limpar)
limparB.place(x= 270, y = 150, anchor=CENTER)
AlunoB = Button(janela, text="Aluno", command=aluno)
AlunoB.place(x= 330, y = 150, anchor=CENTER)


janela.mainloop()

