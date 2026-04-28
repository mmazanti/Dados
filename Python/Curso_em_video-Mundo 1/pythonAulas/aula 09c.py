frase = 'Curso em Vídeo Python'
print(frase.replace('Python', 'Android'))
#Uma string e seus micro-elementos é imutável. A não ser que eu utilize uma função e a atribua a uma variável.
print(frase.find('Java'))
print(frase.find('Vídeo'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))
print('Curso' in frase)
frase_dividido = frase.split()
print(frase_dividido[0])
print(frase_dividido[2][3])
