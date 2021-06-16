import math
from collections import defaultdict

contagem = defaultdict(int)
def moedas(v, valor):
    contagem[valor] += 1
    if valor in v:
        return 1

    menor = math.inf
    for ma in v:
        if valor-ma > 0:
            solAtual = moedas(v, valor-ma)+1
            if solAtual < menor:
                menor = solAtual
        #menor = min(moedas(v, valor-ma)+1, menor)

    return menor

print(moedas([10,6,5,1], 12))
print(contagem)


