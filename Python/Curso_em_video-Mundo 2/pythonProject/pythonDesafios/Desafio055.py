#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#-A média de idade do grupo;
#-Qual o nome do homem mais velho;
#-Quantas mulheres têm menos de 20 anos.
soma_idade = 0
maior_idade_homem = 0
nome_homem_mais_velho = ""
mulheres_sub20 = 0
for pessoa in range(0, 4):
    nome = str(input('Digite o seu nome: ')).strip()
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma_idade += idade
    if sexo == 'M':
        if maior_idade_homem == 0 or idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_homem_mais_velho = nome
    elif sexo == 'F' and idade < 20:
        mulheres_sub20 += 1
media_idade = soma_idade / 4
print('A média de idade do grupo é de {:.1f} anos.'.format(media_idade))
if nome_homem_mais_velho != " ":
    print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, nome_homem_mais_velho))
else:
    print('Não foram registrados homens neste grupo.')
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheres_sub20))
