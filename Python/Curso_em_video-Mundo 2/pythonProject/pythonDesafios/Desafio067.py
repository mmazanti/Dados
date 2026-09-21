#Faça um programa que jogue para ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
vitórias = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
while True:
    print('=-' * 20)
    computador = randint(0, 11)
    jogador_número = int(input('Digite um valor: '))
    total = jogador_número + computador
    jogador_palpite = ' '
    while jogador_palpite not in 'PI':
        jogador_palpite = str(input('Par ou ìmpar? [P/I] ')).upper().strip()
    print(f'Você jogou {jogador_número} e o computador {computador}. Total de {total}.')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if jogador_palpite == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitórias += 1
        else:
            print('Você PERDEU!')
            break
    if jogador_palpite == 'I':
        if total % 2 == 1:
            print('Voce VENCEU!')
            vitórias += 1
        else:
            print('Voce PERDEU!')
            break
    print('Vamos jogar novamente...')
if vitórias == 1:
    print(f'GAME OVER! Você venceu {vitórias} vez.')
elif vitórias > 1:
    print(f'GAME OVER! Você venceu {vitórias} vezes.')
else:
    print(f'GAME OVER! Você venceu nenhuma vez!')