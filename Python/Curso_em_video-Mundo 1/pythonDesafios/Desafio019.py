#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos aluno. Faça um programa que leia
#o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
aluno_1 = input('Digite o nome do primeiro aluno: ')
aluno_2 = input('Digite o nome do segundo aluno: ')
aluno_3 = input('Digite o nome do terceiro aluno: ')
aluno_4 = input('Digite o nome do quarto aluno: ')
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
sortear = shuffle(lista)
print('A ordem da apresentação será: \n1° {} \n2° {} \n3° {} \n4° {}'.format(lista[0], lista[1], lista[2], lista[3]))
