saque = int(input("Digite o valor do saque R$: "))

if saque < 10 or saque > 600:
  print("Valor fora do intervalo, digite um valor de saque válido!")
else:
  nota_100 = saque / 100
  nota_50 = (int(saque) % 100)/50
  nota_10 = ((int(saque) % 100) % 50)/10
  nota_5 = (((int(saque) % 100) % 50) % 10)/5
  nota_1 = ((((int(saque) % 100) % 50) % 10) %5)/1


  print("")
  print("A quantidade de notas de R$ 100 é de: ",int(nota_100))
  print("A quantidade de notas de R$ 50 é de: ",int(nota_50))
  print("A quantidade de notas de R$ 10 é de: ",int(nota_10))
  print("A quantidade de notas de R$ 5 é de: ",int(nota_5))
  print("A quantidade de notas de R$ 1 é de: ",int(nota_1))