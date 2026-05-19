#Crie um programa que faça o computador jogar JOKENPÔ com você.
import random
jokenpô_lista = ["PEDRA", "PAPEL", "TESOURA"]
jokenpô_cpu = random.choice(jokenpô_lista)
jokenpô_usuário = str(input('Vamos jogar jokenpô? Escolha: PEDRA, PAPEL ou TESOURA?: ')).strip().upper()
if jokenpô_cpu == 'PEDRA' and jokenpô_usuário == 'PEDRA':
    print('{} empata com {}. Ninguém ganhou.'.format(jokenpô_cpu, jokenpô_usuário))
elif jokenpô_cpu == 'PEDRA' and jokenpô_usuário == 'PAPEL':
    print('{} perde de {}. VOCÊ GANHOU!'.format(jokenpô_cpu, jokenpô_usuário))
elif jokenpô_cpu == 'PEDRA' and jokenpô_usuário == 'TESOURA':
    print('{} ganha de {}. VOCÊ PERDEU!'.format(jokenpô_cpu, jokenpô_usuário))
elif jokenpô_cpu == 'PAPEL' and jokenpô_usuário == 'PAPEL':
    print('{} empata com {}. Ninguém ganhou.'.format(jokenpô_cpu, jokenpô_usuário))
elif jokenpô_cpu == 'PAPEL' and jokenpô_usuário == 'TESOURA':
    print('{} perde de {}. VOCÊ GANHOU!'.format(jokenpô_cpu, jokenpô_usuário))
elif jokenpô_cpu == 'PAPEL' and jokenpô_usuário == 'PEDRA':
    print('{} ganha de {}. VOCÊ PERDEU!'.format(jokenpô_cpu, jokenpô_usuário))
elif jokenpô_cpu == 'TESOURA' and jokenpô_usuário == 'TESOURA':
    print('{} empata com {}. Ninguém ganhou.'.format(jokenpô_cpu, jokenpô_usuário))
elif jokenpô_cpu == 'TESOURA' and jokenpô_usuário == 'PEDRA':
    print('{} perde de {}. VOCÊ GANHOU!'.format(jokenpô_cpu, jokenpô_usuário))
elif jokenpô_cpu == 'TESOURA' and jokenpô_usuário == 'PAPEL':
    print('{} ganha de {}. VOCÊ PERDEU!'.format(jokenpô_cpu, jokenpô_usuário))
else:
    print('Escolha uma opção válida entre PEDRA, PAPEL e TESOURA.')
