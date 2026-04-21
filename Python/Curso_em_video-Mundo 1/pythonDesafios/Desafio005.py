#Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ele.
escrita = input('Digite algo: ')
print(type(escrita))
print('{} é um número?'.format(escrita), escrita.isalnum())
print('{} é uma letra?'.format(escrita), escrita.isalpha())
print('{} está em maiúsculo?'.format(escrita), escrita.isupper())
print('{} está em minúsculo?', escrita.islower())
