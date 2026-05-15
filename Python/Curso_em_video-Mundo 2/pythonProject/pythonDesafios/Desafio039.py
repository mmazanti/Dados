#Crie um programa que leia duas notas de um aluno e calcule sua média mostrando uma mensagem no final de acordo com a média atingida:
#-Média abaixo de 5.0: REPROVADO
#-Média entre 5.0 e 6.9: RECUPERAÇÃO
#-Média 7.0 ou superior: APROVADO
nota_1 = float(input('Qual o valor da primeira nota? '))
nota_2 = float(input('Qual o valor da segunda nota? '))
média = (nota_1 + nota_2) / 2
if média < 5.0:
    print('Sua média é de {}. Você está REPROVADO!'.format(média))
elif média >= 5.0 and média < 7.0:
    print('Sua média é de {}. Você está de RECUPERAÇÃO!'.format(média))
else:
    print('Sua média é de {}. Parabéns! Você está APROVADO!'.format(média))
