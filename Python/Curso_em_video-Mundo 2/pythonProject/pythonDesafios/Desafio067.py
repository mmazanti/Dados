#Faça um programa que jogue para ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
vitórias = 0
derrota = False
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
while derrota == False:
    print('=-' * 20)
    computador = randint(0, 10)
    jogador_número = int(input('Diga um valor: '))
    jogador_palpite = input('Par ou ìmpar? [P/I] ').upper().strip()
    par_ou_impar = jogador_número + computador
    print('-' * 20)
    if par_ou_impar % 2 == 0 and jogador_palpite == 'P':
        print(f'Você jogou {jogador_número} e o computador {computador}. Total de {par_ou_impar} DEU PAR.')
        print('-' * 20)
        print('Você VENCEU!')
        vitórias += 1
        print('Vamos jogar novamente...')
    elif par_ou_impar % 2 == 0 and jogador_palpite == 'I':
        print(f'Você jogou {jogador_número} e o computador {computador}. Total de {par_ou_impar} DEU PAR.')
        print('-' * 20)
        print('Você PERDEU!')
        derrota = True
    elif par_ou_impar % 1 == 0 and jogador_palpite == 'I':
        print(f'Você jogou {jogador_número} e o computador {computador}. Total de {par_ou_impar} DEU IMPAR.')
        print('-' * 20)
        print('Você VENCEU!')
        vitórias += 1
        print('Vamos jogar novamente...')
    elif par_ou_impar % 1 == 0 and jogador_palpite == 'P':
        print(f'Você jogou {jogador_número} e o computador {computador}. Total de {par_ou_impar} DEU IMPAR.')
        print('-' * 20)
        print('Você PERDEU!')
        derrota = True
print('=-' * 20)
if vitórias == 1:
    print(f'GAME OVER! Você venceu {vitórias} vez.')
elif vitórias > 1:
    print(f'GAME OVER! Você venceu {vitórias} vezes.')
else:
    print(f'GAME OVER! Você venceu nenhuma vez!')
