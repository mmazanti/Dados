#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#-À vista dinheiro/PIX: 10% DE DESCONTO
#-À vista no cartão: 5% DE DESCONTO
#-Em até 2x no cartão: PREÇO NORMAL
#-3x ou mais no cartão: 20% DE JUROS
preço = float(input('Qual o valor do produto? '))
condição_pagamento = int(input('Qual a forma de pagamento? \n#1 à vista (dinheiro/PIX) \n#2 à vista no cartão \n#3 Parcelado 2x no cartão \n#4 Parcelado 3x ou mais no cartão \nDigite a opção escolhida: '))
if condição_pagamento == 1:
    preço_desconto = preço - (preço * 0.10)
    print('Para pagamento à vista, o produto que custava R${:.2f} custará {:.2f}.'.format(preço, preço_desconto))
elif condição_pagamento == 2:
    preço_desconto = preço - (preço * 0.05)
    print('Para pagamento à vista, o produto que custava R${:.2f} custará {:.2f}.'.format(preço, preço_desconto))
elif condição_pagamento == 3:
    print('Parcelado 2x no cartão o produto continuará custando R${:.2f}.'.format(preço))
elif condição_pagamento == 4:
    preço_juros = preço + (preço * 0.20)
    print('Parcelado 3x ou mais no cartão o produto que custava R${:.2f} terá 20% de juros passando a custar R${:.2f}.'.format(preço, preço_juros))
else:
    print('Selecione uma opção válida entre 1, 2, 3, 4.')
