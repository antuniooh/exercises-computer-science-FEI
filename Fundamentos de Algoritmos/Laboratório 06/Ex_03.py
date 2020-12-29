
# coding: utf-8

# In[1]:


def retorno():
    arquivo = open("numeros_6_3.txt", "r")
    soma = 0
    elementos = 0
    for linha in arquivo.readlines():
        linhaInt = int(linha)
        elementos += 1
        soma += linhaInt
    print("A soma dos números é: ", soma)
    print("A média dos números é: ", soma/elementos)

def main():
    retorno()

main()
    

