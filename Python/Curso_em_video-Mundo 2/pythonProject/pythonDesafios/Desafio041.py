#Refaça o DESAFIO 035 dos triângulos, acrescentado o recurso de mostrar que tipo de triângulo será formado:
#-EQUILÁTERO: todos os lados iguais
#-ISÓSCELES: Dois lados iguais
#-ESCALENO: todos os lados diferentes.
reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('Esses 3 seguimentos de retas podem formar um triângulo.')
    if reta1 == reta2 and reta1 == reta3:
        print('Esse triângulo é EQUILÁTERO.')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Esse triângulo é ISÓSCELES.')
    else:
        print('Esse triângulo é ESCALENO.')
else:
    print('Esses 3 seguimentos de retas não podem formar um triângulo.')