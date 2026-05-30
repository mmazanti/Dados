#Melhore o Desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
print('=*'*11)
print('PROGRESSÃO ARITMÉTICA')
print('=*'*11)
termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
contagem_termo = 1
progressão_aritimética = termo
qtde_termo = 10
while contagem_termo <= qtde_termo:
    print(f'{progressão_aritimética}', end=' ➔ ')
    progressão_aritimética += razão
    contagem_termo += 1
menu_sn = input('Quer saber mais termos da PA? [S/N] ').upper().strip()
while menu_sn == 'S':
    qtde_termo += int(input('Quantos termos a mais quer saber?: '))
    while contagem_termo <= qtde_termo:
        print(f'{progressão_aritimética}', end=' ➔ ')
        progressão_aritimética += razão
        contagem_termo += 1
    menu_sn = input('Quer saber mais termos da PA? [S/N] ').upper().strip()
else:
    print('Fim da PA.')
