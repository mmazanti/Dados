#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado por ímpar, desconsidere-o
soma = 0
contagem = 0
for laço in range(1, 7):
    numero = int(input('Digite o {}º número: '.format(laço)))
    if numero % 2 == 0:
        soma += numero
        contagem += 1
if contagem == 1:
    print('Você digitou {} número PAR e a soma foi de {}'.format(contagem, soma))
elif contagem > 1:
    print('Você digitou {} números PARES e a soma foi de {}'.format(contagem, soma))
else:
    print('Você digitou nenhum número PAR.')
