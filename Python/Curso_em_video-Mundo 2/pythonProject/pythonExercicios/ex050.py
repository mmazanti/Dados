#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado por ímpar, desconsidere-o.
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
if cont == 1:
    print('Você digitou {} número PAR e a soma foi de {}'.format(cont, soma))
elif cont > 1:
    print('Você digitou {} números PARES e a soma foi de {}'.format(cont, soma))
else:
    print('Você digitou nenhum número PAR.')
