#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
#vai informar quantas cédulas de cada valor serão entregues.
#OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('='*30)
print(' '*7, 'BANCO MASTER')
print('='*30)
valor_saque = int(input('Que valor você quer sacar? R$ '))
cédula_50 = valor_saque // 50
valor_saque = valor_saque % 50
cédula_20 = valor_saque // 20
valor_saque = valor_saque % 20
cédula_10 = valor_saque // 10
valor_saque = valor_saque % 10
cédula_1 = valor_saque // 1
print(f'Total de {cédula_50} cédulas de R$50')
print(f'Total de {cédula_20} cédulas de R$20')
print(f'Total de {cédula_10} cédulas de R$10')
print(f'Total de {cédula_1} cédulas de R$1')
print('='*30)
print('Volte sempre ao BANCO MASTER! Tenha um bom dia!')
