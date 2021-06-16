#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Antono Muniz      22.119.001-0
#Atividade 3


# In[5]:


#ex 2

#Sabe-se que 60% dos indivíduos submetidos a um tratamento médico sobrevivem. 
#Se 20 indivíduos foram submetidos ao tratamento, determine, aplicando a 
#distribuição binomial, a probabilidade de no máximo dois sobreviverem.


# In[6]:


from scipy.stats import binom
t = binom.pmf(2, 20, 6/10) + binom.pmf(1, 20, 6/10) + binom.pmf(0, 20, 6/10)
print(t)


# In[7]:


#ex 3
#O número de mortes por afogamento em fins de semana, numa cidade praiana, 
#é de 2 a cada grupo de 50000 habitantes em média.


# In[8]:


#a - Qual a probabilidade de que em um grupo de 200000 habitantes ocorram 5 afogamentos?


# In[9]:


from scipy.stats import binom
binom.pmf(5,200000,2/50000)


# In[10]:


#b - Qual a probabilidade de que em um grupo de 125000 habitantes ocorram pelo menos 3 afogamentos? 


# In[11]:


from scipy.stats import binom
print(1 - (binom.pmf(2,125000,2/50000) + binom.pmf(1,125000,2/50000) + binom.pmf(0,125000,2/50000) ) )


# In[15]:


#ex 4
#Uma empresa de eletrônicos considerou que o tempo de vida de suas baterias de celular 
#segue uma distribuição normal com média de 120 minutos e variância de 100 minutos.

#media = 120
#var = 100
#desvio padrão é a raiz quadrada da variância = 10


# In[16]:


#a - Qual é a probabilidade aproximada de uma bateria durar menos que 100 minutos?


# In[17]:


from scipy.stats import norm
#P(x < 100)
norm.cdf(100,120,10)


# In[18]:


#b - Qual é a probabilidade de uma bateria durar 115 e 130 minutos?


# In[19]:


#P(115 < x < 130)
norm.cdf(130,120,10) - norm.cdf(115,120,10) 

