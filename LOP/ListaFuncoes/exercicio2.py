import numpy as np

maior_idade = 0
criancas_menores_5_anos = 0
adultos = 0

idades = np.zeros(10, dtype = int)

def calc_media_idades(lista_idades):
    media = np.mean(lista_idades)
    return media

for i in range(0, 10):
    idade = int(input(f"Entrevistado(a) número {i+1}, quantos anos você tem?: "))
    idades[i] = idade

    if idade > maior_idade:
        maior_idade = idade

    if idade < 5:
        criancas_menores_5_anos += 1

    elif idade > 18:
       adultos += 1

media_idades = calc_media_idades(idades)

print(f"A média de idade dos entrevistados é de: {media_idades} anos")
print(f"A quantidade de entrevistados que tem menos de 5 anos é de: {criancas_menores_5_anos}")
print(f"A quantidade de entrevistados que tem mais de 18 anos é de: {adultos}")
print(f"A maior de idade dentre os entrevistados é de: {maior_idade} anos")
