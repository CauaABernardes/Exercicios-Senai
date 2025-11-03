qtd_mulheres = 0
qtd_homens = 0
media_idades = 0
media_idade_homens = 0
mulheres_com_mais_de_20_anos = 0

for i in range (0, 5):
    sexo = input("Qual é o seu sexo (M/F): ")
    if sexo.upper() in ["M","MASCULINO","HOMEM"]:
        qtd_homens += 1
        idade = int(input("Digite a sua idade: "))
        media_idade_homens += idade
        media_idades += idade
    elif sexo.upper() in ["F", "FEMININO", "MULHER"]:
        qtd_mulheres += 1
        idade = int(input("Digite a sua idade: "))
        media_idades += idade
        if idade > 20:
            mulheres_com_mais_de_20_anos += 1

media_idades = media_idades / 5
media_idade_homens = media_idade_homens / qtd_homens

print(f"A quantidade de homens cadastrados foi de: {qtd_homens}\nA quantidade de mulheres cadastradas foi de: {qtd_mulheres}")
print(f"A média de idade dos cadastrados foi de: {media_idades} anos")
print(f"A média de idade dos homens cadastrados foi de: {media_idade_homens} anos")
print(f"Ao total tivemos {mulheres_com_mais_de_20_anos} mulhere(s) com mais de 20 anos cadastradas")