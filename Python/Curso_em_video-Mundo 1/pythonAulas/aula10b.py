nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2) / 2
print('A sua média foi {:.1f}.'.format(média))
#print('PARABÉNS' if média >= 6 else 'ESTUDE MAIS')
if média >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS')