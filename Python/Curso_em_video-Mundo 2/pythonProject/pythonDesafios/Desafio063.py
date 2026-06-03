#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999
#que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag).
qtde_número = soma = 0
número = int(input('Digite um número (para parar digite 999): '))
menu = número
while número != 999:
    qtde_número += 1
    soma += número
    número = int(input('Digite um número (para parar digite 999): '))
print(f'Você digitou um total de {qtde_número} números e a soma dos números digitados é de {soma}')
