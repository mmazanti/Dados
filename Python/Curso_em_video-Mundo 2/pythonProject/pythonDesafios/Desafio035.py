#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa vai perguntar o valor da casa,
#o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder
#30% do salário ou então o empréstimo será negado.
valor_casa = float(input('Qual o valor do imóvel? '))
salário = float(input('Qual o valor do seu salário? R$ '))
anos_pagamento = int(input('Em quantos anos você pretende pagar? '))
prestação = valor_casa / (anos_pagamento * 12)
if prestação > salário * 0.30:
    print('Renda incompatível com o valor do imóvel. EMPRÉSTIMO NEGADO.')
else:
    print('Empréstimo aprovado! O valor da prestação será de R${:.2f}.'.format(prestação))