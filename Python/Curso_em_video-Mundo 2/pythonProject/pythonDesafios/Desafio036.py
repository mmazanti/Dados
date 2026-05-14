#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#-1 para binário
#-2 para octal
#-3 para hexadecimal.
número = int(input('Digite um número: '))
base_conversão = int(input('Qual será a base de conversão? \n#1 para binário \n#2 para octal \n#3 para hexadecimal \nDigite: '))
if base_conversão == 1:
    print('O número {} em binário é {:b}.'.format(número, número))
elif base_conversão == 2:
    print('O número {} em octal é {:o}.'.format(número, número))
elif base_conversão == 3:
    print('O número {} em hexadecimal é {:x}.'.format(número, número))
else:
    print('Opção inválida. Tente novamente escolhendo as opções 1, 2 ou 3.')
