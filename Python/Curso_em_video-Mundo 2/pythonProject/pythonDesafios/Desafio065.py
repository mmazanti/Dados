#Crie um programa que leia vários número inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag).
número = soma = contador = 0
while número != 999:
    número = int(input('Digite um valor (999 para parar): '))
    if número == 999:
        break
    soma += número
    contador += 1
print(f'Você digitou {contador} números, e a soma entre eles é de {soma}')
