#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#-Se ele ainda vai se alistar ao serviço militar.
#-Se é a hora de se alistar.
#-Se já passou do tempo de alistamento.
#-O programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import datetime
ano_atual = datetime.now().year
ano_nascimento = int(input('Em que ano você nasceu? '))
if ano_atual - ano_nascimento == 18:
    print('Chegou o ano de você se alistar no exército.')
elif ano_atual - ano_nascimento < 18:
    if (ano_atual - ano_nascimento) - 18 <= 1:
        ano_excedente = 18 - (ano_atual - ano_nascimento)
        print('Você ainda não completou 18 anos. Faltam {} ano para você se alistar'.format(ano_excedente))
    else:
        ano_excedente = 18 - (ano_atual - ano_nascimento)
        print('Você ainda não completou 18 anos. Faltam {} anos para você se alistar'.format(ano_excedente))
elif ano_atual - ano_nascimento > 18:
    if (ano_atual - ano_nascimento) - 18 == 1:
        ano_excedente = (ano_atual - ano_nascimento) - 18
        print('Você passou {} ano do prazo para o seu alistamento militar.'.format(ano_excedente))
    else:
        ano_excedente = (ano_atual - ano_nascimento) - 18
        print('Você passou {} anos do prazo para seu alistamento militar.'.format(ano_excedente))
