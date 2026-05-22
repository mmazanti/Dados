#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderendo os espaço.
import unicodedata
frase = str(input('Digite uma frase: '))
frase_tratada = frase.lower().replace(" ", "")
frase_tratada = unicodedata.normalize('NFD', frase_tratada)
frase_tratada = "".join(ch for ch in frase_tratada if unicodedata.category(ch) != 'Mn')
frase_invertida = frase_tratada[::-1]
if frase_tratada == frase_invertida:
    print('A frase {} É UM PALÍNDROMO!'.format(frase))
else:
    print('A frase {} NÃO É UM PALÍNDROMO!'.format(frase))
