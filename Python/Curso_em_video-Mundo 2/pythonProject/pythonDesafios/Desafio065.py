#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior
#e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
qtde_valores = 0
maior_valor = 0
menor_valor = 0
soma_valores = 0
menu = 'S'
while menu == 'S':
    valor = int(input('Digite um número: '))
    qtde_valores += 1
    soma_valores += valor
    if qtde_valores == 1:
        maior_valor = valor
        menor_valor = valor
    else:
        if valor > maior_valor:
            maior_valor = valor
        elif valor < menor_valor:
            menor_valor = valor
    menu = input('Quer continuar [S/N] ').upper().strip()
média = soma_valores / qtde_valores
print(f'Você digitou um total de {qtde_valores} números. A média de todos esses números é de {média}. O maior número foi o {maior_valor} e o menor número foi o {menor_valor}')
