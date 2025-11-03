nums_no_intervalo = 0

for _ in range(10):
    num_digitado = float(input("Digite um número: "))

    if num_digitado >= 10 and num_digitado <= 20:
        nums_no_intervalo += 1

print(f"A quantidade de números no intervalo de 10 a 20 digitados foram: {nums_no_intervalo}")