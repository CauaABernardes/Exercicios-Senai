largura = float(input("Digite a largura de seu terreno (em metros): "))
comprimento = float(input("Digite o compremento de seu terreno (em metros):"))

if largura <= 0 or comprimento <= 0:
    print("Medidas inválidas, não existe largura ou comprimento menor ou igual à zero")

else:
    area = largura * comprimento

    if area < 100:
        print(f"O seu terreno de {area}m² é um terreno Popular")
    elif area <= 500:
        print(f"O seu terreno de {area}m² é um terreno Master")
    else:
        print(f"O seu terreno de {area}m² é um terreno VIP")
