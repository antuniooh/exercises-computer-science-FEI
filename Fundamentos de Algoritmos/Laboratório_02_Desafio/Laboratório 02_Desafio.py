x_entrada = int(input("x: "))
y_entrada = int(input("y: ")) 
z_entrada = int(input("z: "))

x = x_entrada
y = y_entrada
z = z_entrada

if x > y:
    temp = x
    x = y
    y = temp

if y > z:
    temp = y
    y = z
    z = temp
    
if x > y:
    temp = x
    x = y
    y = temp

print("Ordenado (crescente)")    
print (x) 
print (y)
print (z)
print()
print("Original, conforme entrada") 
print (x_entrada) 
print (y_entrada)
print (z_entrada)