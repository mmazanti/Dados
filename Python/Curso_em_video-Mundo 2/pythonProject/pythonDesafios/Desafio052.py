#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderendo os espaço.
from unicodedata import normalize, category
frase = str(input('Digite uma frase: '))
frase_tratada = frase.lower().replace(" ", "")
frase_tratada = normalize('NFD', frase_tratada)
frase_tratada = "".join(ch for ch in frase_tratada if category(ch) != 'Mn')
frase_invertida = frase_tratada[::-1]
if frase_tratada == frase_invertida:
    print('A frase {} É UM PALÍNDROMO!'.format(frase))
else:
    print('A frase {} NÃO É UM PALÍNDROMO!'.format(frase))
