#!/usr/bin/env python
# coding: utf-8

# In[ ]:


matriz = []

for num_linha in range(3):
    linha=[]
    for num_coluna in range(3):
        linha.append("0")
    matriz.append(linha)

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print("%2s" % matriz[linha][coluna], end=" ")
    print()
    
def main():
    o = "O"
    x = "X"

    
    def OO():
        pos = int(input("Digite a posição do jogador O: "))
        
        def O1():
                if pos == 1 :
                    matriz[0][0] = o
                elif pos == 2:
                    matriz[0][1] = o
                elif pos == 3 :
                    matriz[0][2] = o
                elif pos == 4:
                    matriz[1][0] = o
                elif pos == 5 :
                    matriz[1][1] = o
                elif pos == 6 :
                    matriz[1][2] = o
                elif pos == 7 :
                    matriz[2][0] = o
                elif pos == 8 :
                    matriz[2][1] = o
                elif pos == 9:
                    matriz[2][2] = o 
        
        if pos < 1 or pos > 9:
            print("Posição inavlida")
        else:
            O1()
            
    def XX():
        pos = int(input("Digite a posição do jogador X: "))
        
        def X1():
                if pos == 1 :
                    matriz[0][0] = x
                elif pos == 2:
                    matriz[0][1] = x
                elif pos == 3 :
                    matriz[0][2] = x
                elif pos == 4:
                    matriz[1][0] = x
                elif pos == 5 :
                    matriz[1][1] = x
                elif pos == 6 :
                    matriz[1][2] = x
                elif pos == 7 :
                    matriz[2][0] = x
                elif pos == 8 :
                    matriz[2][1] = x
                elif pos == 9:
                    matriz[2][2] = x 
                    
        if pos < 1 or pos > 9:
            print("Posição inavlida")
        else:
            X1()
             
    def printar():   
        for linha in range(len(matriz)):
            for coluna in range(len(matriz[linha])):
                print("%2s" % matriz[linha][coluna], end=" ")
            print()
    
    #conferir a vitoria
    while matriz[0][0:2] != x :
        XX()
        printar()
        OO()
        printar()
    else:
        print("Jogador X venceu")
    
                
    
            

main()


# In[ ]:




