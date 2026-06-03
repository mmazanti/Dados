#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci.
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
número = int(input('Quantos termos você quer mostrar? '))
contagem_fibonacci = 3
fibonacci_1 = 0
fibonacci_2 = 1
print(f'{fibonacci_1} ➡️ {fibonacci_2}', end='')
while contagem_fibonacci <= número:
    fibonacci_3 = fibonacci_1 +fibonacci_2
    print(f'➡️ {fibonacci_3}', end='')
    fibonacci_1 = fibonacci_2
    fibonacci_2 = fibonacci_3
    contagem_fibonacci += 1
print('➡️ FIM')
print('-'*30)
