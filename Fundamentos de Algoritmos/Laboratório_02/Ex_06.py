
# coding: utf-8

# In[26]:


x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))
z = int(input("Digite o terceiro valor: "))

#anulando possibilidades diferentes
if x == y and x == z:
    print("Os valores digitados são iguais")
    print("")
    print("Os valores digitados foram: ", x, y, z)
    
if x == y and x < z:
    print("O maior valor é: ", z)
    print("")
    print("Os valores digitados foram: ", x, y, z)
    
if x == y and x > z:
    print("O menor valor é: ", z)
    print("")
    print("Os valores digitados foram: ", x, y, z)
    
if x == z and x < y:
    print("O maior valor é: ", y)
    print("")
    print("Os valores digitados foram: ", x, y, z)
    
if x == z and x > y:
    print("O menor valor é: ", y)
    print("")
    print("Os valores digitados foram: ", x, y, z)
    
if y == z and x > y:
    print("O maior valor é: ", x)
    print("")
    print("Os valores digitados foram: ", x, y, z)
    
if y == z and x < y:
    print("O maior valor é: ", x)
    print("")
    print("Os valores digitados foram: ", x, y, z)
    
    
# Ordem Crescente
if x > y and x > z and y > z:
    print("Os valores em ordem crescente: ", z, y, x)
    print("")
    print("Os valores digitados foram: ", x, y, z)
    
if x > y and x > z and y < z:
    print("Os valores em ordem crescente: ", y, z, x)
    print("")
    print("Os valores digitados foram: ", x, y, z)
    
if x > y and x < z:
    print("Os valores em ordem crescente: ", y, x, z)
    print("")
    print("Os valores digitados foram: ", x, y, z)
    
if x < y and x < z and y < z:
    print("Os valores em ordem crescente: ", x, y, z)
    print("")
    print("Os valores digitados foram: ", x, y, z)
    
if x < y and x < z and y > z:
    print("Os valores em ordem crescente: ", x, z, y)
    print("")
    print("Os valores digitados foram: ", x, y, z)
    
if x < y and x > z and y > z:
    print("Os valores em ordem crescente: ", z, x, y)
    print("")
    print("Os valores digitados foram: ", x, y, z)
    
    

