PRECO_DIARIA_CARRO_POPULAR = 90
PRECO_KM_CARRO_POPULAR = 0.20
PRECO_KM_CARRO_POPULAR_ACIMA_100 = 0.10

PRECO_DIARIA_CARRO_LUXO = 150
PRECO_KM_CARRO_LUXO = 0.30
PRECO_KM_CARRO_LUXO_ACIMA_200 = 0.25

print("+===============================+")
print("|       Carros do Marquin       |")
print("|===============================|")
print("| 1 - Aluguel de Carro Popular: |")
print("| 2 - Aluguel de Carro Luxo...: |")
print("| 3 - Sair....................: |")
print("+===============================+")

opcao = int(input("Digite a sua opção desejada: "))

if opcao == 1:
    qtd_dias = int(input("Digite a quantiadade de dias que o carro foi alugado: "))
    kms_percorridos = float(input("Digite quantos KM foram percorridos durante o aluguel: "))

    if qtd_dias <= 0 or kms_percorridos <= 0:
        print("Valores inválidos")
    else:
        valor_diaria = qtd_dias * PRECO_DIARIA_CARRO_POPULAR

        if kms_percorridos <= 100:
            valor_km = (kms_percorridos * PRECO_KM_CARRO_POPULAR)

        else:
            valor_km = (kms_percorridos * PRECO_KM_CARRO_POPULAR_ACIMA_100)

        valor_total = (valor_diaria + valor_km)

        print(f"O valor total do aluguel do carro popular foi de: R$ {valor_total}\nObrigado pela preferência :)")

elif opcao == 2:
    qtd_dias = int(input("Digite a quantiadade de dias que o carro foi alugado: "))
    kms_percorridos = float(input("Digite quantos KM foram percorridos durante o aluguel: "))

    if qtd_dias <= 0 or kms_percorridos <= 0:
        print("Valores inválidos")
    else:
        valor_diaria = qtd_dias * PRECO_DIARIA_CARRO_LUXO

        if kms_percorridos <= 200:
            valor_km = (kms_percorridos * PRECO_KM_CARRO_LUXO)

        else:
            valor_km = (kms_percorridos * PRECO_KM_CARRO_LUXO_ACIMA_200)

        valor_total = (valor_diaria + valor_km)

        print(f"O valor total do aluguel do carro popular foi de: R$ {valor_total}\nObrigado pela preferência :)")

elif opcao == 3:
    print("Te vejo na próxima :)")

else:
    print("Opção inválida")