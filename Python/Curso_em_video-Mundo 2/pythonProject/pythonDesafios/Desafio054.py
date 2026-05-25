#Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior_peso = 0
menor_peso = 0
for pessoa in range(1, 6):
    peso = float(input('Digite o seu peso: '))
    if pessoa == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso
print('O maior peso lido foi: {}kg'.format(maior_peso))
print('O menor peso lido foi: {}kg'.format(menor_peso))
