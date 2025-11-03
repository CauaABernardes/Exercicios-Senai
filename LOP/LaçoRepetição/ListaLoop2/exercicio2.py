maior_idade = 0
idades = []
criancas_menores_5_anos = 0
adultos = 0
media_idades = 0

for i in range(0, 10):
    idade = int(input(f"Entrevistado(a) número {i+1}, quantos anos você tem?: "))
    idades.append(idade)

    if idade > maior_idade:
        maior_idade = idade

    if idade < 5:
        criancas_menores_5_anos += 1

    elif idade > 18:
       adultos += 1

for idade in idades:
    media_idades += idade

media_idades = media_idades/10

print(f"A média de idade dos entrevistados é de: {media_idades} anos")
print(f"A quantidade de entrevistados que tem menos de 5 anos é de: {criancas_menores_5_anos}")
print(f"A quantidade de entrevistados que tem mais de 18 anos é de: {adultos}")
print(f"A maior de idade dentre os entrevistados é de: {maior_idade} anos")
