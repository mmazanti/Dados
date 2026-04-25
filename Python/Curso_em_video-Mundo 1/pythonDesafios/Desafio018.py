#Um professor quer sortear um dos seus quatro alunos para apagar um quadro. Faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
aluno_1 = input('Digite o nome do primeiro aluno: ')
aluno_2 = input('Digite o nome do segundo aluno: ')
aluno_3 = input('Digite o nome do terceiro aluno: ')
aluno_4 = input('Digite o nome do quarto aluno: ')
print('O aluno sorteado para apagar o quadro é o {}.'.format(choice([aluno_1, aluno_2, aluno_3, aluno_4])))
