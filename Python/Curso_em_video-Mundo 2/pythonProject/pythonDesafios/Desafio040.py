#A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#-Até 9 anos: MIRIM
#-Até 14 anos: INFANTIL
#-Até 19 anos: JÚNIOR
#-Até 20 anos: SÊNIOR
#-Acima: MASTER
from datetime import datetime
ano_atual = datetime.now().year
ano_nascimento = int(input('Em que ano você nasceu? '))
idade = ano_atual - ano_nascimento
if idade <= 9:
    print('{} anos. Categoria: MIRIM.'.format(idade))
elif idade > 9 and idade <= 14:
    print('{} anos. Categoria: INFANTIL.'.format(idade))
elif idade > 14 and idade <= 19:
    print('{} anos. Categoria: JÚNIOR.'.format(idade))
elif idade > 19 and idade <= 20:
    print('{} anos. Categoria: SÊNIOR.'.format(idade))
else:
    print('{} anos. Categoria: MASTER.'.format(idade))
