#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#-Abaixo de 18.5: ABAIXO DO PESO
#-Entre 18.5 até 25:: PESO IDEAL
#-Entre 25 até 30: SOBREPESO
#-Entre 30 até 40: OBESIDADE
#-Acima de 40: OBESIDADE MÓRBIDA
peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite a sua altura em m: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('ABAIXO DO PESO! Procure um médido.')
elif imc >= 18.5 and imc < 25:
    print('PESO IDEAL.')
elif imc >= 25 and imc < 30:
    print('SOBREPESO.')
elif imc >= 30 and imc <= 40:
    print('OBESIDADE.')
else:
    print('OBESIDADE MÓRBIDA! Procure um médico.')