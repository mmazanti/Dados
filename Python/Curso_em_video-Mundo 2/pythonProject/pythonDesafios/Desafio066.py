#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando  número solicitado for negativo.
número = int(input('Quer ver a tabuada de qual valor? '))
while número >= 0:
    print('-'*10)
    for c in range(1, 11):
        print(f'{número} X {c} = {número * c}')
    print('-' * 10)
    número = int(input('Quer ver a tabuada de qual valor? '))
    if número < 0:
        break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
