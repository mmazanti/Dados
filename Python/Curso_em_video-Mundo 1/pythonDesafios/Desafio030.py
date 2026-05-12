#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km
#para viagens de até 200Km e R$ 0,45 para viagens mais longas.
distancia = float(input('Qual a distância da sua viagem? '))
if distancia <= 200:
    valor_passagem = distancia * 0.5
    print('A sua passagem vai custar R${:.2f}.'.format(valor_passagem))
else:
    valor_passagem = distancia * 0.45
    print('A sua passagem vai custar R${:.2f}.'.format(valor_passagem))