#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando  número solicitado for negativo.
while True:
    número = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*10)
    if número < 0:
        break
    for c in range(1, 11):
        print(f'{número} X {c} = {número * c}')
    print('-' * 10)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
