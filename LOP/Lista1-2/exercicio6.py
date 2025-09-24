dist_viagem = float(input("Digite quantos kilômetros você deseja viajar: "))

valor_viagem = 0

if dist_viagem <= 0:
    print("Distância inválida")
elif dist_viagem <= 200:
    valor_viagem = dist_viagem * 0.50
    print(f"O valor total da viagem foi de: R$ {valor_viagem:.2f}")
else:
    valor_viagem = dist_viagem * 0.45
    print(f"O valor total da viagem foi de: R$ {valor_viagem:.2f}")
