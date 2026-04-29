#Faça um programa que leia um frase pelo teclado e mostre:
#- Quantas vezes aparece a letra "A".
#- Em que posição ela aparece a primeira vez.
#- Em que posição ela aparece a última vez.
frase = input('Digite uma frase: ')
print("A letra 'A' aparece {} vez(es) na frase.".format(frase.count('A')))
print("A letra 'A' aparece a primeira vez na posição {}.".format(frase.find('A')))
print("A letra 'A' aparece a última vez na posição {}.".format(frase.rfind('A')))
