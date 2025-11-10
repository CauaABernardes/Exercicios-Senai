chegou_no_quadrado = False
quadrado_alcancado = 0
num = 1

numero_digitado = int(input("Digite o número que deseja saber o quadrado dele: "))

quadrado_requisitado = numero_digitado ** 2

while not chegou_no_quadrado:
    quadrado_alcancado += num
    num += 2

    if quadrado_alcancado == quadrado_requisitado:
        chegou_no_quadrado = True

print(f"O número {numero_digitado} tem como seu quadrado {quadrado_alcancado}")