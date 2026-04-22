#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario_base = float(input('Qual o valor do seu salário atual?: '))
salario_aumento = salario_base+(salario_base * 0.15)
print('O valor do seu salário com o aumento de 15% será de R$ {}'.format(salario_aumento))
