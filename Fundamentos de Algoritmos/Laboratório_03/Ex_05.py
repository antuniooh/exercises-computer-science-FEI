idade = input("Digite a idade do visitante: ")
valor = 0

while idade != "":
  idade = input("Digite a idade do visitante: ")

  if idade > 0 and idade <=2:
    valor += 0.00
  elif idade > 2 and idade <= 12:
    valor += 14.00
  elif idade >= 65:
    valor += 18.00
  else:
    valor += 23.00

print("O valor do ingresso de todos os vistantes é de R$ ", valor)
