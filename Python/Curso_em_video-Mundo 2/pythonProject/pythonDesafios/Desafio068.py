#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#No final, mostre:
#A) Quantas pessoas tem mais de 18 anos.
#B) Quantos homens foram cadastrados.
#C) Quantas mulheres tem menos de 20.
stop = 'S'
maior_18 = 0
homens = 0
mulheres = 0
while stop == 'S':
    print('-'*30)
    print(' '*5, 'CADASTRE UMA PESSOA', ' '*5)
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').upper().strip()
    if idade >= 18:
        maior_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    stop = input('Quer continuar? [S/N] ').upper().strip()
print('='*5, 'FIM DO PROGRAMA', '='*5)
print(f'Total de pessoas com mais de 18 anos: {maior_18}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres} mulheres com menos de 20 anos.')
