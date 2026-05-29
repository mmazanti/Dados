#Refaça o desafio 51 lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('=*'*11)
print('PROGRESSÃO ARITMÉTICA')
print('=*'*11)
termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
contagem_termo = 1
progressão_aritimética = termo
while contagem_termo <= 10:
    print(f'{progressão_aritimética}', end=' ➔ ')
    progressão_aritimética += razão
    contagem_termo += 1
print('Fim da PA.')
