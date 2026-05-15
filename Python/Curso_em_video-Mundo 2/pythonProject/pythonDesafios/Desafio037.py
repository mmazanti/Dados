#Escreva um programa que leia dois número inteiros e compare-os mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#-Não existe valor maior, os dois são iguais.
número_1 = int(input('Digite um número: '))
número_2 = int(input('Digite outro número: '))
if número_1 > número_2:
    print('O primeiro número é o maior.')
elif número_2 > número_1:
    print('O segundo número é o maior.')
else:
    print('Não existe valor maior. Os dois são iguais.')