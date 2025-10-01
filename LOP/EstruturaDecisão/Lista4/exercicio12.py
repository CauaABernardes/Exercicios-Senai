km_percorrido = float(input("Digite quantos kilômetros foram percorridos: "))
litros_gasolina_gastos = float(input("Digite quantos litros foram consumidos durante o trajeto: "))

litragem = km_percorrido/litros_gasolina_gastos

if km_percorrido <= 0 or litros_gasolina_gastos <= 0:
    print("Dados inválidos")

else:
    print(f"O consumo de gasolina do seu carro é de: {litragem:.2f} km/l")
    if litragem < 8:
        print("Venda o carro!")

    elif litragem <= 12:
        print("Econômico!")

    else:
        print("Super econômico!")