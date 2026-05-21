#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
número = int(input('Digite um número: '))
total_divisores = 0
for intervalo_primo in range(1, número + 1):
    if número % intervalo_primo == 0:
        total_divisores += 1
if total_divisores == 2:
    print('O número {} É PRIMO!'.format(número))
else:
    print('O número {} NÃO É PRIMO!'.format(número))
