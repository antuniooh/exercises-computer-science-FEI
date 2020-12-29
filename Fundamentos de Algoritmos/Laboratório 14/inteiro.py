#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      anton
#
# Created:     22/05/2019
# Copyright:   (c) anton 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def isInteger(palavra):
    if len(palavra) >=1:
        for x in range(len(palavra)):
            if palavra[x] == "." or palavra[x] ==",":
                print("Não é inteiro")
            else:
                if palavra[0] == "-":
                    if int(palavra[1:])// 1 == int(palavra[1:]):
                        print("É inteiro")
                elif palavra[0] == "+":
                    if int(palavra[1:])// 1 == int(palavra[1:]):
                        print("É inteiro")
                elif int(palavra)// 1 == int(palavra):
                    print("É inteiro")
    else:
        print("Não é inteiro")
