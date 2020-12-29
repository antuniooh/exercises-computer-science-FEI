#!/usr/bin/env python
# coding: utf-8

# In[1]:


def primeiroExemplo():
    print("Vez do jogador 1 - Números correspondentes as casas:")
    print("      1 | 2 | 3 ")
    print("     ---+---+---")
    print("      4 | 5 | 6 ")
    print("     ---+---+---")
    print("      7 | 8 | 9 ")


def jogoANDexemplo(a,b,c,d,e,f,g,h,i,rodada,jogador):
    print("RODADA %d - Vez do jogador %d  -   Números correspondentes as casas:" % (rodada,jogador))
    print(" %s | %s | %s       1 | 2 | 3 " % (a,b,c))
    print("---+---+---     ---+---+---")
    print(" %s | %s | %s       4 | 5 | 6 " % (d,e,f))
    print("---+---+---     ---+---+---")
    print(" %s | %s | %s       7 | 8 | 9 " % (g,h,i))


print("--- JOGO DA VELHA ---")

primeiroExemplo()

a = " "
b = " "
c = " "
d = " "
e = " "
f = " "
g = " "
h = " "
i = " "

rodada = 1
contagem = 9
while contagem > 0:
    
    contagempi = contagem % 2
    
    if contagempi == 1: #X
        entrada = int(input("Insira o número correspondente a casa:"))
        
        if entrada == 1:
            a = "X"
            
        elif entrada == 2:
            b = "X"
            
        elif entrada == 3:
            c = "X"
            
        elif entrada == 4:
            d = "X"
            
        elif entrada == 5:
            e = "X"
            
        elif entrada == 6:
            f = "X"
            
        elif entrada == 7:
            g = "X"
            
        elif entrada == 8:
            h = "X"
            
        elif entrada == 9:
            i = "X"
            
        else:
            print("Entrada inváida!")
            print("Finalizando jogo!")
            break
        
        jogador = contagempi + 1
        
        jogoANDexemplo(a,b,c,d,e,f,g,h,i,rodada,jogador)
        
        rodada = rodada + 1
        contagem = contagem - 1
        
    if contagempi == 0: #O
        entrada = int(input("Insira o número correspondente a casa:"))
        
        if entrada == 1:
            a = "O"
            
        elif entrada == 2:
            b = "O"
            
        elif entrada == 3:
            c = "O"
            
        elif entrada == 4:
            d = "O"
            
        elif entrada == 5:
            e = "O"
            
        elif entrada == 6:
            f = "O"
            
        elif entrada == 7:
            g = "O"
            
        elif entrada == 8:
            h = "O"
            
        elif entrada == 9:
            i = "O"
            
        else:
            print("Entrada inváida!")
            print("Finalizando jogo!")
            break
        
        jogador = contagempi + 1
        
        jogoANDexemplo(a,b,c,d,e,f,g,h,i,rodada,jogador)
        
        rodada = rodada + 1
        contagem = contagem - 1

    if a == "X" and e == "X" and i == "X":
        break
    elif c == "X" and e == "X" and g == "X":
        break
    elif a == "X" and d == "X" and g == "X":
        break
    elif b == "X" and e == "X" and h == "X":
        break
    elif c == "X" and f == "X" and i == "X":
        break
    elif a == "X" and b == "X" and c == "X":
        break
    elif d == "X" and e == "X" and f == "X":
        break
    elif g == "X" and h == "X" and i == "X":
        break
        
    if a == "O" and e == "O" and i == "O":
        break
    elif c == "O" and e == "O" and g == "O":
        break
    elif a == "O" and d == "O" and g == "O":
        break
    elif b == "O" and e == "O" and h == "O":
        break
    elif c == "O" and f == "O" and i == "O":
        break
    elif a == "O" and b == "O" and c == "O":
        break
    elif d == "O" and e == "O" and f == "O":
        break
    elif g == "O" and h == "O" and i == "O":
        break
        
if contagem == 0:
    print(" --- EMPATE ---")
    print("--- GAME OVER ---")
    
elif contagempi == 0:
    print("O Jogador que reprenta o [O] ganhou o jogo!")
    print("--- GAME OVER ---")
    
elif contagempi == 1:
    print("O Jogador que reprenta o [X] ganhou o jogo!")
    print("--- GAME OVER ---")

