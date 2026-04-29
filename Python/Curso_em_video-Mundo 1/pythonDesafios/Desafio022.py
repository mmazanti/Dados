#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
número = input('Digite um número de 0 a 9999: ')
print('O número {} decomposto é:'.format(número))
print('Unidade: {}'.format(número[3]))
print('Dezena: {}'.format(número[2]))
print('Centena: {}'.format(número[1]))
print('Milhar: {}'.format(número[0]))
