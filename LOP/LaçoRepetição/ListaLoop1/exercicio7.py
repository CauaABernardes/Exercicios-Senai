n = int(input("Digite um número (deve ser maior que 0): "))

while n <= 0:
    print("Não são aceitos valores nulos ou negativos para o número requisitado!")
    n = int(input("Digite um número (deve ser maior que 0): "))

for i in range(1, n + 1):
    print(i)
