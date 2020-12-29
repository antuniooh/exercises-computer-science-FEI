#!/usr/bin/env python
# coding: utf-8

# In[118]:


def ler():
    #abrir o arquivo
    arquivo = open("usuarios.txt", 'r+') 
        
    #ler o arquivo e armazenar numa lista
    cliente = arquivo.readlines() 
    
    #lista só com os bytes
    byte = []
    user = []
    
    # adicionar a lista byte o valor dos clientes
    for x in range(len(cliente)):
        valor = ""
        # pegar o número dentro da lista
        for numero in cliente[x]:
            if numero.isdigit():
                valor += numero 
        byte.append(valor)    
    
    #adicionar a uma lista  o  nome dos cliente
    for x in range(len(cliente)):
        c = cliente[x].split()
        user.append(c[0])
        
    # valor total
    totalB = 0.0
    for x in range(len(byte)):
        totalB += int(byte[x])
    totalB = totalB/1048576
    
    # media
    tamanho = len(cliente)
    totalC = float(tamanho)
    media = totalB/tamanho
        
    # metodo escrever
    def escrever():
        #caso esteja exibe o nome, cpf, tipo de conta do cliente e todas as movimentações
        print("XFiles            Uso do espaço em disco pelos usuários")
        print("-------------------------------------------------------")
        print("NR.  Usuário            Espaço Utilizado         % do uso")
        #fazer a conversão e a porcentagem
        for x in range(1,len(cliente)):
            b = float(byte[x])/1048576
            porcentagem = (b * 100)/totalB
            print("{0:>1}{1:>10}{2:>25.2f} MB {3:>15.2f} %" .format(x,user[x],b,porcentagem) )
        print("")
        print("Espaço Total Ocupado: %.2f MB" % totalB)
        print("Espaço Médio Ocupado: %.2f MB" % media)    
        
    #fecha-se o arquivo e salva
    arquivo.close()
    
    escrever()

def main():
    ler()

main()
    


# In[ ]:





# In[ ]:




