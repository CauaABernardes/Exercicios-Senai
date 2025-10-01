numero = input("Digite um número de 4 dígitos: ")

if len(numero) != 4 or numero == "0000":
    print("Número inválido")

else:
    numero_invertido = (numero[3] + numero[2] + numero[1] + numero[0])

    print(f"O número: {numero} invertido é igual à: {numero_invertido}")
