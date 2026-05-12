#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
#qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
numero = randint(0, 5)
palpite = int(input('Em que número estou pensando de 0 a 5?: '))
if numero == palpite:
    print('Parabéns, você acertou! O número que pensei é o {}.'.format(numero))
else:
    print('Você errou! O número que eu pensei é o {}.'.format(numero))