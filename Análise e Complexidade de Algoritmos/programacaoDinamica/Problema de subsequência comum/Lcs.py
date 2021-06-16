from collections import defaultdict

contagem = defaultdict(int)

def LCS(s1,s2):
    contagem[ (s1,s2) ] +=1
    #Caso Base
    if len(s1)==0 or len(s2)==0:
        return 0

    #Passo Recursivo
    if s1[-1] == s2[-1]:
        return LCS(s1[:-1], s2[:-1])+1
    else:
        return max(LCS(s1[:-1], s2), LCS(s1, s2[:-1]))

print(LCS("flavio", "balaio"))
print(contagem)

