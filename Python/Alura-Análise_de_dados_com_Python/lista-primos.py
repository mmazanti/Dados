primo = []
limite_lista = int(input("Digite um numero inteiro: "))
while True:
    for divisor in range(1, limite_lista+1):
        qtde_divisor = 0
        for dividendo in range(1, divisor+1):
            if divisor % dividendo == 0:
                qtde_divisor += 1
        if qtde_divisor == 2:
            primo.append(divisor)
    if divisor == limite_lista:
        break
print(f'Os números primos entre 1 e {limite_lista} são: {primo}')