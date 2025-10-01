lado_A = float(input("Digite o valor do Lado 'A': "))
lado_B = float(input("Digite o valor do Lado 'B': "))
lado_C = float(input("Digite o valor do Lado 'C': "))

if lado_A <= 0 or lado_B <= 0 or lado_C <= 0:
    print("Não é possível se formar um triângulo")

else:

    if lado_A >= (lado_B + lado_C) or lado_B >= (lado_A + lado_C) or lado_C >= (lado_A + lado_B):
        print("Não é possível se formar um triângulo")

    else:
        if lado_A == lado_B and lado_A == lado_C:
            print("O triângulo é equilátero")

        elif ((lado_A == lado_B) and (lado_A != lado_C)) or ((lado_A == lado_C) and (lado_A != lado_B)) or ((lado_B == lado_C) and (lado_B != lado_A)):
            print("O triângulo é isóceles")

        else:
            print("O triângulo é escaleno")