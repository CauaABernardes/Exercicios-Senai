velocidade = int(input("Digite qual é a velocidade do carro: "))

if velocidade > 80:
    velocidade_aux = velocidade - 80
    multa = (velocidade_aux*5)
    print(f"A multa do carro foi de: R${multa}")
else:
    print("Não houve multa")