from collections import defaultdict
from functools import cache

contagens = defaultdict(int)


@cache
def MC(precos, tam):
    contagens[tam]+=1
    valorAgregado = 0
    opcaoEscolhida = [-1]
    for i in range(1,len(precos)):
        sobra = tam - i
        if sobra  >= 0:
            valor = precos[i]
            valorSobras, opcaorec = MC(precos, sobra)
            if valor+valorSobras > valorAgregado:
                valorAgregado = valor+valorSobras
                opcaoEscolhida = [*opcaorec, i]

    return valorAgregado, opcaoEscolhida

precos = (0,1,5,8,9,10,17,17,20)
a, b = MC(precos, 10)
print(a)
print(b)


def MCProgDin(precos, tam):
    cache_opt = [0]*(tam+1)
    cache_esc = [0]*(tam+1)
    for i in range(1, tam+1):
        for c in range(1,len(precos)):
            sobra = i - c
            if sobra >= 0:
                valor = precos[c]+cache_opt[sobra]
                if valor > cache_opt[i]:
                    cache_opt[i] = valor
                    cache_esc[i] = c
    return cache_opt, cache_esc


a, b = MCProgDin(precos, 10)
print(a)
print(b)

