#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado por ímpar, desconsidere-o
soma = 0
for contagem in range(0, 6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma += numero
print('A soma de todos os números pares que você digitou é de {}.'.format(soma))
