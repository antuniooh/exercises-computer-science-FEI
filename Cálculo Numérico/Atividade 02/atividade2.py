#!/usr/bin/env python
# coding: utf-8

# In[41]:


#Nome: Antonio Gustavo Muniz
#RA: 22.119.001-0

#Calculo Numerico - Atividade 02


# In[17]:


import numpy as np
from sympy import Matrix, solve_linear_system
from sympy.abc import x,y,z

matriz_A = np.matrix([[3,5,1],[2,2,2],[4,7,3]])
matriz_b=([1],[3],[0])
matrizA_inv=np.linalg.inv(matriz_A)
sol=matrizA_inv*matriz_b
print("Resolução com a inevrsa:")
print(sol)

system=Matrix(( (3,5,1,1), (2,2,2,3),(4,7,3,0) ))
print("Resolução com o solve_linear_system:")
solve_linear_system(system, x, y, z)


# In[18]:


import numpy as np
matriz_A = np.matrix([[1,1,1,1,1],[1,2,3,4,5],
                      [1,3,6,10,15],[1,4,10,20,35],
                      [1,5,15,35,70]])
matriz_b=([[15],[35],[70],[126],[210]])

matrizA_inv=np.linalg.inv(matriz_A)
sol=matrizA_inv*matriz_b
print("Resolução com a inversa:")
print(sol)

solB=np.linalg.solve(matriz_A, matriz_b)
print("Resolução com o solve:")
print(solB)


# In[19]:


import numpy as np
a=np.matrix([[200,100,500],[250,120,400],
            [400,80,600]])
b=([[495.00],[532.50],[585.00]])

sol=np.linalg.inv(a)*b
print("Valor da libra esterlina: ")
print(sol[1])


# In[38]:


from sympy import Matrix, solve_linear_system
from sympy.abc import x,y,z,t
import numpy as np

system=Matrix(( (2,8,4,0,-1), (4,-6,-2,-10, -14),
               (6, -14, 2, -10, -16), (0,2,-2,-2,-2) ))
print("Resolução do sistema linear: ")
solve_linear_system(system, x, y, z,t)


# In[47]:


print("Como é possivel observar, as variaveis nao ",
      "foram totalmente resolvidas, logo é um sistema",
      "indeterminado\n")

matriz_A = np.matrix([
[2,8,4,0],
[4,-6,-2,-10],
[6,-14,2,-10],
[0,2,-2,-2]])

matriz_B = ([[-1],[-14],[-16],[-2]])
det = np.linalg.det(matriz_A)
print("determinante desse sistema")
print(det)
sol = np.linalg.solve(matriz_A, matriz_B)
print("\nResolvendo o sistema anterior com solve:")
print(sol)

matrizA_inv=np.linalg.inv(matriz_A)
sol2=matrizA_inv*matriz_B
print("\nResolução com a inversa:")
print(sol2)

sol3=np.linalg.solve(matriz_A, matriz_B)
print("\nResolução com o solve:")
print(sol3)


# In[ ]:




