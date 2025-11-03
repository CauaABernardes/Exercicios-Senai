soma_nums = 0

for i in range(1, 11):
    num = float(input(f"Digite o {i}ª num: "))
    if num < 40:
        soma_nums += num


print(f"A soma total de números abaixo de 40 é de: {soma_nums:.2f}")