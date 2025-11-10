import numpy as np

qtd_mulheres = 0
qtd_homens = 0

idades = np.zeros(10, dtype = int)

media_idade_homens = 0
mulheres_com_mais_de_20_anos = 0

def calc_media_idade(lista_idades):
    media = np.mean(lista_idades)
    return media

for i in range (0, 5):
    sexo = input("Qual é o seu sexo (M/F): ")
    if sexo.upper() in ["M","MASCULINO","HOMEM"]:
        qtd_homens += 1
        idade = int(input("Digite a sua idade: "))
        media_idade_homens += idade
        idades[i] = idade
    elif sexo.upper() in ["F", "FEMININO", "MULHER"]:
        qtd_mulheres += 1
        idade = int(input("Digite a sua idade: "))
        idades[i] = idade
        if idade > 20:
            mulheres_com_mais_de_20_anos += 1

media_idades = calc_media_idade(idades)

media_idade_homens = media_idade_homens / qtd_homens

print(f"A quantidade de homens cadastrados foi de: {qtd_homens}\nA quantidade de mulheres cadastradas foi de: {qtd_mulheres}")
print(f"A média de idade dos cadastrados foi de: {media_idades:.2f} anos")
print(f"A média de idade dos homens cadastrados foi de: {media_idade_homens} anos")
print(f"Ao total tivemos {mulheres_com_mais_de_20_anos} mulhere(s) com mais de 20 anos cadastradas")