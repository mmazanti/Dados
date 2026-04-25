#Faça um programa que leia um ângul qualquer e mostre na tela o valor do seno, cosseno e tangento desse Ângulo.
from math import sin, cos, tan, radians
ângulo = float(input('Digite o valor do ângulo: '))
radiano = radians(ângulo)
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)
print('O ângulo de {} tem o seno de {:.2f}, o cosseno de {:.2f} e a tangente de {:.2f}.'.format(ângulo, seno, cosseno, tangente))
