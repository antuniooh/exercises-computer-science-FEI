
# coding: utf-8

# In[1]:


from palavra import aleatoria

def main():
    p = aleatoria()
    erros = 6
    t1 = []
    digitadas = ""

    #criar list t1 #desenhar os pontinhos
    for x in range(len(p)):
        t1 += p[x]
    for y in range(len(t1)):
        t1[y] = "."
    
    print(p)
    def impressão():
        if erros == 6:
                print("X==:==")
                print("X  :  ")
                print("X     ")
                print("X     ")
                print("X     ")
                print("X     ")
                print("======")               
        elif erros == 5:
                print("X==:==")
                print("X  :  ")
                print("X  0  ")
                print("X     ")
                print("X     ")
                print("X     ")
                print("======")
        elif erros == 4:
                print("X==:==")
                print("X  :  ")
                print("X  0  ")
                print("X  |  ")
                print("X     ")
                print("X     ")
                print("======")
        elif erros == 3:
                print("X==:==")
                print("X  :  ")
                print("X  0  ")
                print("X \|  ")
                print("X     ")
                print("X     ")
                print("======")         
        elif erros == 2:
                print("X==:==")
                print("X  :  ")
                print("X  0  ")
                print("X \|/ ")
                print("X     ")
                print("X     ")
                print("======")         
        elif erros == 1:
                print("X==:==")
                print("X  :  ")
                print("X  0  ")
                print("X \|/ ")
                print("X /   ")
                print("X     ")
                print("======")
        else:
                print("X==:==")
                print("X  :  ")
                print("X  0  ")
                print("X \|/ ")
                print("X / \ ")
                print("X     ")
                print("======")
                print("Enforcado!")
            
        print(t1)
        print("Letras já digitadas: ", digitadas)
        print("")
    
    while erros > 0: 
        ponto = "."
        if ponto not in t1:
            print("Você Ganhou!")
            break
        else:
            letra = input("Digite uma letra: ")
        
            #lista da string de digitadas
            d = []
            d = digitadas.replace(","," ").split()
        
            #caso a letra não esteja em digitadas e esteja na palavra
            if letra in p and letra not in d:
                digitadas += letra + ","
                for x in range(len(p)):
                    if letra == p[x]:
                        t1[x] = letra
            elif letra in d:
                print("Letra repetida")
            else:
                print("Você errou!")
                erros -=1

            impressão()   


if __name__ =="__main__":
    main()

