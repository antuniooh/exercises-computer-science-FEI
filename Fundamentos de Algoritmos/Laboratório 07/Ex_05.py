#!/usr/bin/env python
# coding: utf-8

# In[22]:


Turma =[[[10, 8 , 10, 8],[10, 8 , 10, 8],[10, 8 , 10, 8],[10, 8 , 10, 8],[10, 8 , 10, 8],[10, 8 , 10, 8],[10, 8 , 10, 8],[10, 8 , 10, 8]
        ],[[10, 8 , 10, 8],[10, 8 , 10, 8],[10, 8 , 10, 8],[10, 8 , 10, 8],[10, 8 , 10, 8],[10, 8 , 10, 8],[10, 8 , 10, 8],[10, 8 , 10, 8]],[[10, 8 , 10, 8],[10, 8 , 10, 8],[10, 8 , 10, 8],[10, 8 , 10, 8],[10, 8 , 10, 8],[10, 8 , 10, 8],[10, 8 , 10, 8],[10, 8 , 10, 8]]]


        
print("AlunosTurmaA:" , Turma[0])
print("")
print("AlunosTurmaB:" , Turma[1])
print("")
print("AlunosTurmaC:" , Turma[2])
print("")
print("")

def MediaAluno(Turma):
    
    print("Média cada Aluno Turma A: ")
    soma = 0
    for y in range(0,8):
        for x in range(0,4):
            soma += Turma[0][y][x]
        print("A média do aluno é:", soma/4)
        soma = 0
    print("") 
    
    print("Média cada Aluno Turma B: ")
    for y in range(0,8):
        for x in range(0,4):
            soma += Turma[1][y][x]
        print("A média do aluno é:", soma/4)
        soma = 0
    print("") 
    
    print("Média cada Aluno Turma C: ")
    for y in range(0,8):
        for x in range(0,4):
            soma += Turma[2][y][x]
        print("A média do aluno é:", soma/4)
        soma = 0
    print("") 
    
def MediaTurma(Turma):
    soma = 0
    for y in range(0,8):
        for x in range(0,4):
            soma += Turma[0][y][x]
    print("Média da turma A:", soma/32)
    soma=0
    
    for y in range(0,8):
        for x in range(0,4):
            soma += Turma[1][y][x]
    print("Média da turma B:", soma/32)
    soma=0
    
    for y in range(0,8):
        for x in range(0,4):
            soma += Turma[2][y][x]
    print("Média da Turma C:", soma/32)
    soma=0
    
def main():
    MediaAluno(Turma)
    MediaTurma(Turma)
    
main()


# In[ ]:




