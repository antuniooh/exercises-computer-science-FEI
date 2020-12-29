#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input("Digite um número inteiro entre 0 e 999: "))




def converter(numero):
    resultado = ""
    
    #dicionario das centenas com o cem individual
    centenas = {
            "0": "",
            "1": "cento e",
            "2": "duzentos e",
            "3": "trezentos e",
            "4": "quatrocentos e",
            "5": "quinhentos e",
            "6": "seiscentos e",
            "7": "setecentos e",
            "8": "oitocentos e",
            "9": "novecentos e",
            100: "cem",
            200: "duzentos",
            300: "trezentos",
            400: "quatrocentos",
            500: "quinhentos",
            600: "seiscentos",
            700: "setecentos",
            800: "oitocentos",
            900: "novecentos"

    }
    #casa das dezenas     
    #casa das dezenas entre 10 e 19
    dezenas ={
            "0": "",
            "2": " vinte",
            "3": " trinta",
            "4": " quarenta",
            "5": " cinquenta",
            "6": " sessenta",
            "7": " setenta",
            "8": " oitenta",
            "9": " noventa",
            "10": " dez",
            "11": " onze",
            "12": " doze",
            "13": " treze",
            "14": " quatorze",
            "15": " quinze",
            "16": " dezesseis",
            "17": " dezessete",
            "18": " dezoito",
            "19": " dezenove"
    }

    #unidades no geral
    unidades = {
            "0": "",
            "1": " e um",
            "2": " e dois",
            "3": " e tres",
            "4": " e quatro",
            "5": " e cinco",
            "6": " e seis",
            "7": " e sete",
            "8": " e oito",
            "9": " e nove",
            0: "zero",
            1: "um",
            2: "dois",
            3: "tres",
            4: "quatro",
            5: "cinco",
            6: "seis",
            7: "sete",
            8: "oito",
            9: "nove"
        }
    
    #se o numero está dentro do intervalo solicitado
    if numero > 999 or numero < 0:
        print("Número inválido")
    else:
        #se ele for menor que nove adiciona-se duas casa a erquerda e converte pra str
        if numero < 9:
            numero_s = "00" + str(numero)
        #se ele for entre 10 e 100 adiciona-se uma casa a erquerda e converte pra str
        elif numero > 9 and numero < 100:
            numero_s = "0" + str(numero)
            #caso contrario trabalha-se normal
        else:
            numero_s = str(numero)
            
            
        #caso o numero seja o caso especial das centenas
        numero_int = int(numero_s)
        if numero_int % 100 == 0:
            resultado += centenas[numero_int]
        #caso seja o especial das unidades
        elif numero_int >= 0 and numero_int < 10:
            resultado += unidades[numero_int]
            
        #caso contrario trabalha-se o passo a passo
        else:
            #primeiro analisa-se a centena e atribui um valor
            for chave, valor in centenas.items():
                if numero_s[0] == chave:
                    resultado += valor
                    
            # pega as duas ultimas casas (decimal e unidade), para entrar no caso da faixa 10-19
            dez = int(numero_s[1:3])
            
            #caso ele seja maior que 10 e menor que 20
            if dez > 9 and dez < 20:
                #avalia se o intervalo das duas casa é igual ao do dicionário
                for chave, valor in dezenas.items():
                    if numero_s[1:3] == chave:
                        resultado += valor
            #caso não seja entre 10-19 trabalha-se normal
            else:
                #confere a unidade da casa decimal
                for chave, valor in dezenas.items():
                    if numero_s[1] == chave:
                        resultado += valor
                    else:
                        pass
                #confere a unidade da casa das unidades
                for chave, valor in unidades.items():
                    if numero_s[2] == chave:
                        resultado += valor
    #ao final exibe o resultado na string resultado que acumulou todos os nomes ao longo da function
    print("Resultado: ", resultado)
    
converter(n)
        


# In[ ]:




