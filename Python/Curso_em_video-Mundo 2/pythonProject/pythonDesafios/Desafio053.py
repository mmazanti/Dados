#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import datetime
ano_atual = datetime.now().year
maior_idade = 0
for c in range(0, 6):
    ano_nascimento = int(input('Em que ano você nasceu? '))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maior_idade += 1
print('Das 7 pessoas, {} são maiores de idade.'.format(maior_idade))
