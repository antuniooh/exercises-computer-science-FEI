#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os

menu = int(input("Digite o q deseja fazer: "))

def Criar():
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")
    telefone = int(input("Digite o telefone: "))
    email = input("Digite o email: ")
    
    arquivo = open(nome +"_" + sobrenome + ".txt", 'w')
    arquivo.write("Telefone: %d \n" % telefone)
    arquivo.write("Email: %s" % email)
    arquivo.close()
    
    global menu
    menu = int(input("Digite o q deseja fazer: "))
    
def Procurar():
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")

    
    arquivo = open(nome +"_"+ sobrenome + ".txt", 'r')
    print("")
    for linha in arquivo.readlines():
        print(linha)
    arquivo.close()

        
    global menu
    menu = int(input("Digite o q deseja fazer: "))
    
def Atualizar():
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")

    
    arquivo = open(nome +"_"+ sobrenome + ".txt", 'r+')
    print("")
    for linha in arquivo.readlines():
        print(linha)
    
    os.remove(nome + "_" + sobrenome + ".txt")
                
    telefone = int(input("Digite o novo telefone: "))
    email = input("Digite o novo email: ")

    arquivo = open(nome +"_" + sobrenome + ".txt", 'w')
    arquivo.write("Telefone: %d \n" % telefone)
    arquivo.write("Email: %s" % email)
    arquivo.close()

    
    
    global menu
    menu = int(input("Digite o q deseja fazer: "))

def Apagar():
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")

    os.remove(nome + "_" + sobrenome + ".txt")

    
    global menu
    menu = int(input("Digite o q deseja fazer: "))


def main():
    while True:
        if menu == 0:
            break
        elif menu == 1:
            Criar()
        elif menu == 2:
            Procurar()
        elif menu == 3:
            Atualizar()
        elif menu == 4:
            Apagar()
        else:
            print("O comando digitado não é valido")
            break
            
main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




