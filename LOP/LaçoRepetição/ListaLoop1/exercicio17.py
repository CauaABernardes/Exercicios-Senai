maior = float(input("Digite um número: "))
menor = maior

for n in range (1, 100):
    num = float(input("Digite um número: "))

    if num > maior:
        maior = num
    elif num < menor:
        menor = num

print(f"O maior número digitado foi o '{maior}', e o menor número digitado foi o '{menor}'")
