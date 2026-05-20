#Refaça o Desafio009 mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for
numero = int(input('Digite um número para saber sua tabuada: '))
for fator in range(0, 11):
    produto = numero * fator
    print('{} X {} = {}'.format(numero, fator, produto))
