from Fuzzy import Fuzzy
from Stab import Stab
from SwingUp import SwingUp

print("1 - Swing Up")
print("2 - Stabilization")

op = 0
while op not in [1, 2]:
    op = int(input("Opcao desejada: "))

angulo = float(input("\n Digite o angulo: "))
velocidade_angular = float(input("velocidade angular: "))

if op == 1:
    obj = SwingUp()
    obj.plot_ante()
    obj.plot_conse()
    swing_up_output = obj.show([angulo, velocidade_angular])

elif op == 2:
    posicao_carro = float(input("Posição do carrinho: "))
    velocidade_carro = float(input("velocidade do carro: "))

    obj = Stab()
    obj.plot_ante()
    obj.plot_conse()
    stabilization_output = obj.show([angulo, velocidade_angular, posicao_carro, velocidade_carro])