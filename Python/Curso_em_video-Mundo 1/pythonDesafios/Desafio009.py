#Escreva um programa que leia um valor em metro e o exiba convertido em centimetros e milímetros.
metro = float(input('Digite o valor em metros: '))
centimetro = metro*100
milimetro = metro*1000
print('{}m equivale a {}cm e {}mm'.format(metro, centimetro, milimetro))