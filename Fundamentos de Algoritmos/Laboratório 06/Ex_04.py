
# coding: utf-8

# In[1]:


num = []
num_unicos = []

def retornoNum():
    arquivo = open("numeros_6_4.txt", "r")
    for linha in arquivo.readlines():
        num.append(int(linha))
    print(num)

def retornoNumUnicos(num):
    for x in num:
        while x not in num_unicos:
            num_unicos.append(x)
    print(num_unicos)
    
def gravaNumUnicos(num_unicos):
    arquivo = open("numeros_6_4_unicos.txt", "w")
    for x in num_unicos:
        arquivo.write("%d \n" % x)


def main():
    retornoNum()
    retornoNumUnicos(num)
    gravaNumUnicos(num_unicos)
    
main()

