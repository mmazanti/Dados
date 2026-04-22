#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária
#para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
largura = float(input('Qual a largura da parede em metros?: '))
altura = float(input('Qual a altura da parede em metros?: '))
tinta = 1*(largura*altura)/2
print('Para pintar essa parede, serão necessários {} litros de tinta.'.format(tinta))