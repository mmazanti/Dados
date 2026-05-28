#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = input('Qual o seu sexo? [M/F] ').upper().strip()
while sexo != 'M' and sexo != 'F':
    sexo = input('Informação inválida! Digite novamente seu sexo detro das opções [M/F] ').upper().strip()
if sexo == 'M':
    sexo = 'Masculino'
else:
    sexo = 'Feminino'
print(f'Seu sexo é {sexo}')
