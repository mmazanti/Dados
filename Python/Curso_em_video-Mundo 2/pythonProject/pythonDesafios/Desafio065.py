#Crie um programa que leia vários número inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag).
soma = contador = 0
while True:
    número = int(input('Digite um valor (999 para parar): '))
    if número == 999:
        break
    contador += 1
    soma += número
print(f'Você digitou {contador} números, e a soma entre eles é de {soma}')
