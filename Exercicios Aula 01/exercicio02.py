#Fazer um programa em que o usuário digita o raio de um circunferência e o programa imprime na tela o seu comprimento.

import math
from math import pi

print('Digite o raio da circunferência: ')
raio = float(input())

comprimento = 2 * raio * pi

print('O comprimento é: {:.2f}'.format(comprimento)) #:.2f arredonda para apenas duas casas decimais
#a variável é colocada no espaço de {}