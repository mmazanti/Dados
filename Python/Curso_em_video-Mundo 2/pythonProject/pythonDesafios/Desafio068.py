#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#No final, mostre:
#A) Quantas pessoas tem mais de 18 anos.
#B) Quantos homens foram cadastrados.
#C) Quantas mulheres tem menos de 20.
stop = 'S'
maior_18 = 0
total_homens = 0
total_mulheres_abaixo_20 = 0
while True:
    print('-'*30)
    print(' '*5, 'CADASTRE UMA PESSOA', ' '*5)
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').upper().strip()
    while sexo != 'M' and sexo != 'F':
            sexo = input('Sexo: [M/F] ').upper().strip()
    if idade >= 18:
        maior_18 += 1
    if sexo == 'M':
        total_homens += 1
    if sexo == 'F' and idade < 20:
        total_mulheres_abaixo_20 += 1
    stop = input('Quer continuar? [S/N] ').upper().strip()
    while stop != 'S' and stop != 'N':
        stop = input('Quer continuar? [S/N] ').upper().strip()
    if stop == 'N':
        break
print('='*5, 'FIM DO PROGRAMA', '='*5)
print(f'Total de pessoas com mais de 18 anos: {maior_18}')
print(f'Total de homens cadastrados: {total_homens}.')
print(f'Total de mulheres com menos de 20 anos cadastradas: {total_mulheres_abaixo_20}')