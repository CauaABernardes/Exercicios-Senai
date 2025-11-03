quer_continuar = True
maior_idade = 0
idade_mulher_mais_nova = float('inf')
qtd_homens = 0
media_idade_homens = 0

while quer_continuar:
    sexo = input("Qual é o sexo do(a) entrevistado(a) (M/F): ")
    if sexo.upper() in ["M", "MASCULINO", "HOMEM"]:
       idade = int(input("Digite a idade do entrevistado: "))
       qtd_homens += 1
       media_idade_homens += idade
       if idade > maior_idade:
           maior_idade = idade
    elif sexo.upper() in ["F", "FEMININO", "MULHER"]:
        idade = int(input("Digite a idade do entrevistado: "))
        if idade > maior_idade:
            maior_idade = idade
        elif idade < idade_mulher_mais_nova:
            idade_mulher_mais_nova = idade


    continua = input("\nDeseja ver mais dados de mais entrevistados? (S/N): ")

    if continua.upper() in ["S","SS", "SIM"]:
        quer_continuar = True
    else:
        quer_continuar = False

media_idade_homens = media_idade_homens / qtd_homens

print(f"\nA maior idade dentre os entrevistados é de {maior_idade} anos")
print(f"Foram entrevistados {qtd_homens} homens")
print(f"A mulher mais jovem tem: {idade_mulher_mais_nova} anos")
print(f"A média de idade dos homens é de: {media_idade_homens}")