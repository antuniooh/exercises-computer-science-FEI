
# coding: utf-8

# In[3]:


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
letra = input("Digite a letra: ")

def media(nota1, nota2, nota3, letra):
    if letra == "A":
        print("Média aritmética: ", (nota1 + nota2 + nota3)/3)
    elif letra == "P":
        print("Média ponderada: ", (nota1 * 5 + nota2 * 3 + nota3 * 2)/10)
    
def main():
    media(nota1, nota2, nota3, letra)
    
main()
            

