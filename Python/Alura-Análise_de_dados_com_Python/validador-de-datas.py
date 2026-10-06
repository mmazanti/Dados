print('='*10, 'VALIDADOR DE DATAS', '='*10)
while True:
    dia = int(input('Digite o dia: '))
    mes = int(input('Digite o mes: '))
    ano = int(input('Digite o ano: '))
    if mes < 1 or mes > 12 or dia < 1 or ano < 1:
        print('DATA INVÁLIDA! Valores fora do limite permitido!')
        continue
    bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        maximo_dias = 31
    elif mes in [4, 6, 9, 11]:
        maximo_dias = 30
    elif mes == 2:
        maximo_dias = 29 if bissexto else 28
    if dia > maximo_dias:
        if mes == 2 and dia == 29:
            print(f'DATA INVÁLIDA! {ano} não é bissexto, Fevereiro tem apenas 28 dias.')
        else:
            print(f'DATA INVÁLIDA! {mes} possui no máximo {maximo_dias} dias.')
    else:
        break
print('='*40)
print(f'A data {dia}/{mes}/{ano} é uma data válida.')