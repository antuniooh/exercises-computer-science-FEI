#!/usr/bin/env python
# coding: utf-8

# In[35]:


s = input("Digite a frase: ")
s = s.lower()
s = s.replace(","," ")
s = s.replace("."," ")
s = s.replace("!"," ")
s = s.split(" ")
print(s)

p1 = ""
p2 =""

#no caso da inicial ser consoante
for x in range(len(s)):
    if s[x][0] !="a" and s[x][0]!="e" and s[x][0] !="i" and s[x][0] !="o" and s[x][0] !="u":
        for y in range(len(s)):
            if s[x][y] =="a" or s[x][y] =="e" or s[x][y] =="i" or s[x][y] =="o" or s[x][y] =="u":
                print(s[x][0:y])
                print(s[x][y:])
                break
    print("Palavra em Pig Latin:", p2 + p1 + "ay")
else:
    print("Palavra em Pig Latin:way")


# In[ ]:




