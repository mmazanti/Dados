#Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
for contagem in range(1, 501):
    if contagem % 2 == 1 and contagem % 3 == 0:
        soma += contagem
print('A soma de todos os números ímpares múltiplos de 3 no range de 1 até 500 é um total de {}.'.format(soma))
