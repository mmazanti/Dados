#Desenvolva um programa que leia o primeiro termo e a razão de PA. No final, mostre os 10 primeiros termos dessa progressão.
print('=*'*11)
print('PROGRESSÃO ARITMÉTICA')
print('=*'*11)
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
décimo_termo = primeiro_termo + (9) * razão
fim_do_range = décimo_termo + razão
for progressão_aritmética in range(primeiro_termo, fim_do_range, razão):
    print(progressão_aritmética)
