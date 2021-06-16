import math
from collections import defaultdict
from functools import cache


count=defaultdict(int)

@cache
def custoMultiplicacao(v, inicio, fim):
    count[(inicio, fim)]+=1

    if inicio == fim:
        return 0

    if fim-inicio==1:
        return v[inicio]*v[fim+1]*v[fim]
    
    menor = math.inf
    for k in range(inicio, fim):
        le = custoMultiplicacao(v, inicio, k)
        ld = custoMultiplicacao(v, k+1, fim)
        custoUniao = v[inicio]*v[fim+1]*v[k+1]
        total = le + ld + custoUniao
        if total < menor:
            menor = total

    return menor
    


def custoMultiplicacaoDin(v):
    c = defaultdict(float)
    numM = len(v)-1
    
    for i in range(0, numM):
        c[i,i]=0

    for i in range(0, numM-1):
        c[i,i+1]= v[i]*v[i+2]*v[i+1]
    

    tam = 3
    for i in range(0, len(v)-tam):
        f = i + tam - 1
        c[i,f] = math.inf
        for k in range(i, f):
            le = c[i,k]
            ld = c[k+1, f]
            uniao = v[i]*v[f+1]*v[k+1]
            total = le+ld+uniao
            if total < c[i,f]:
                c[i,f] = total

    for x in c:
        print(x, c[x])

dim_matrizes = (30, 35, 15, 5, 10, 20, 25)
#custoMultiplicacao(dim_matrizes, 0, 5)

custoMultiplicacaoDin(dim_matrizes)


