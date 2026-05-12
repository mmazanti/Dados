#Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))
if numero1 > numero2 and numero1 > numero3 and numero2 > numero3:
    print('O maior número é o {} e o menor é o {}.'.format(numero1, numero3))
elif numero1 > numero2 and numero1 > numero3 and numero3 > numero2:
    print('O maior número é o {} e o menor é o {}.'.format(numero1, numero2))
elif numero2 > numero1 and numero2 > numero3 and numero1 > numero3:
    print('O maior número é o {} e o menor é o {}.'.format(numero2, numero3))
elif numero2 > numero1 and numero2 > numero3 and numero3 > numero1:
    print('O maior número é o {} e o menor é o {}.'.format(numero2, numero1))
elif numero3 > numero1 and numero3 > numero2 and numero1 > numero2:
    print('O maior número é o {} e o menor é o {}.'.format(numero3, numero2))
elif numero3 > numero1 and numero3 > numero2 and numero2 > numero1:
    print('O maior número é o {} e o menor é o {}.'.format(numero3, numero1))
else:
    print('Os números são iguais.')