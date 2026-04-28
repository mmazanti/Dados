#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse âgulo.
from math import radians, sin, cos, tan
ângulo = float(input('Digite o Ângulo que você deseja: '))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}, COSSENO de {:.2f} e TANGENTE de {:.2f}'.format(ângulo, seno, cosseno, tangente))