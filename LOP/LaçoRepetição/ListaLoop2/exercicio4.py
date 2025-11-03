media_altura = 0
qtd_mais_de_90kg = 0
qtd_menos_de_50kg_e_de_160_altura = 0
qtd_mais_de_100kg_e_de_190_altura = 0
ALTURA_190 = 1.90
ALTURA_160 = 1.60
KG_100 = 100
KG_90 = 90
KG_50 = 50

for i in range(0, 7):
    altura = float(input(f"{i+1}º entrevistado, digite a sua altura (em metros): "))
    if altura > 3:
        altura = altura / 100
    peso = float(input("Agora digite o seu peso (em kg): "))

    media_altura += altura

    if altura > ALTURA_190 and peso > KG_100:
        qtd_mais_de_100kg_e_de_190_altura += 1
        qtd_mais_de_90kg += 1

    elif peso > KG_90:
        qtd_mais_de_90kg += 1

    elif altura < ALTURA_160 and peso < KG_50:
        qtd_menos_de_50kg_e_de_160_altura += 1

media_altura = media_altura / 7

print(f"A média de altura do grupo é de:{media_altura:.2f}m")
print(f"{qtd_mais_de_90kg} pessoas pesam mais de 90kg")
print(f"{qtd_menos_de_50kg_e_de_160_altura} pesam menos de 50kg e tem menos de 1,60m")
print(f"{qtd_mais_de_100kg_e_de_190_altura} pesam mais de 100kg e tem mais de 1,90m")