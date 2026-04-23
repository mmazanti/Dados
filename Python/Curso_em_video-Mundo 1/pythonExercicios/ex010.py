#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. (Considere US$1.00 = R$ 5,00)
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dólar = real / 5.00
euro =  real / 5.84
libra = real / 6.74
print('Com R${:.2f} você pode comprar US${:.2f}, €{:.2f} e £{:.2f}'.format(real, dólar, euro, libra))
