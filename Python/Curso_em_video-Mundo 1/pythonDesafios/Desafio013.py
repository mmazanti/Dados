#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o valor do produto para calcular o desconto: '))
desconto = preco-(preco * 0.05)
print('O valor final do produto com desconto é de R$ {}'.format(desconto))
