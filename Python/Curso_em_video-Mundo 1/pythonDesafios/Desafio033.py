#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salário superiores a R$1.250,00 calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite o valor do seu salário: '))
if salario > 1250:
    novo_salario = salario + (salario * 0.1)
    print('O seu novo salário com o aumento de 10% é de R${:.2f}.'.format(novo_salario))
else:
    novo_salario = salario + (salario * 0.15)
    print('O seu novo salário com o aumento de 15% é de R${:.2f}'.format(novo_salario))