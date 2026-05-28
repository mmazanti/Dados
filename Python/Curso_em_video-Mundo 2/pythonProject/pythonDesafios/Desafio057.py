#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar
#adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
computador = randint(0, 10)
usuário = int(input('Em que número estou pensando de 0 a 10?: '))
tentativa = 1
while computador != usuário:
    usuário = int(input('Você errou! Tente novamente: '))
    tentativa += 1
print(f'Parabéns! Você acertou em {tentativa} tentativas que o número que eu pensei foi o {computador}.')
