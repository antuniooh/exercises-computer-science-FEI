#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      anton
#
# Created:     22/05/2019
# Copyright:   (c) anton 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from conferir import *

def main():
    s = input("Digite a senha: ")
    resultado = []
    resultado.append(str(oito(s)))
    resultado.append(str(maiuscula(s)))
    resultado.append(str(minuscula(s)))
    resultado.append(str(numero(s)))


    fraca = 0

    for x in range(len(resultado)):
        if resultado[x] == "False":
            fraca += 1
        else:
            fraca += 0
    if fraca > 0:
        print("Senha Fraca")
    else:
        print('senha Boa')

if __name__ == '__main__':
    main()
