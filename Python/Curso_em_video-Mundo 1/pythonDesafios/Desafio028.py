#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada Km acima do limite.
velocidade = int(input('Qual a velocidade do veículo?: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você está acima da velocidade permitida da via (80km/h). Sua multa será de R${:.2f}.'.format(multa))
else:
    print('Você está dentro dos limites de velocidade. Boa viagem!')