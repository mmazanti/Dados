#Crie um programa que leia dois valores e mostre um menu na tela:
#[1] Somar
#[2] Multiplicar
#[3] Maior
#[4] Novos números
#[5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
print('-+'*5, 'MENU', '-+'*5)
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
texto_menu = '''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
Escolha uma opção: '''
menu = int(input(texto_menu))

while menu != 5:
    if menu == 1:
        somar = numero1 + numero2
        print(f'{numero1} + {numero2} = {somar}')
    elif menu == 2:
        multiplicar = numero1 * numero2
        print(f'{numero1} x {numero2} = {multiplicar}')
    elif menu == 3:
        if numero1 > numero2:
            print(f'O número {numero1} é maior que o número {numero2}')
        elif numero2 > numero1:
            print(f'O número {numero2} é maior que o número {numero1}')
        else:
            print(f'O número {numero1} e {numero2} são iguais.')
    elif menu == 4:
        numero1 = int(input('Digite um número: '))
        numero2 = int(input('Digite outro número: '))
    else:
        print('Opção inválida!')
    print('-+'*15)
    menu = int(input(texto_menu))
print('-+'*5, 'FIM DO PROGRAMA', '-+'*5)
