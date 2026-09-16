#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:
#A) Qual é o total gasto na compra.
#B) Quantos produtos custam mais de R$ 1.000,00
#C) Qual é o nome do produto mais barato.
print('-'*30)
print(' '*5, 'LOJA SUPER BARATÃO', ' '*5)
print('-'*30)
soma_compra = contador_acima1000 = preço = 0
stop = 'S'
total_produtos = 0
while stop == 'S':
    nome_produto = input('Nome do produto: ').upper().strip()
    preço = float(input('Preço: R$'))
    total_produtos += 1
    #preço_mais_barato = preço
    if preço > 1000:
        contador_acima1000 += 1
    if total_produtos == 1 or preço < preço_mais_barato:
        preço_mais_barato = preço
        nome_produto_mais_barato = nome_produto
    soma_compra += preço
    stop = input('Quer continuar? [S/N] ').upper().strip()
    while stop != 'S' and stop != 'N':
        stop = input('Quer continuar? [S/N] ').upper().strip()
    if stop == 'N':
        break
print('-'*10, ' FIM DO PROGRAMA ', '-'*10)
print(f'O total da compra foi de R${soma_compra:.2f}')
print(f'Temos {contador_acima1000} produtos custando mais de R$1.0000,00')
print(f'O produto mais barato foi {nome_produto_mais_barato} que custa R$ {preço_mais_barato}')