quer_continuar = True
nome_pessoa_mais_velha = ""
maior_idade = 0
nome_mulher_mais_nova = ""
idade_mulher_mais_nova = float('inf')
qtd_homens_mais_30_anos = 0
media_idade = 0
qtd_mulheres_menos_18 = 0
qtd_entrevistados = 0

while quer_continuar:
    sexo = input("Qual é o sexo do(a) entrevistado(a) (M/F): ")
    if sexo.upper() in ["M", "MASCULINO", "HOMEM"]:
        nome = input("Digite o nome do entrevistado: ")
        idade = int(input("Digite a idade do entrevistado: "))

        if idade > maior_idade:
            maior_idade = idade
            nome_pessoa_mais_velha = nome
            if idade > 30:
                qtd_homens_mais_30_anos += 1

        elif idade > 30:
            qtd_homens_mais_30_anos += 1

        media_idade += idade

    elif sexo.upper() in ["F", "FEMININO", "MULHER"]:
        nome = input("Digite o nome da entrevistada: ")
        idade = int(input("Digite a idade da entrevistada: "))

        if idade > maior_idade:
            maior_idade = idade
            nome_pessoa_mais_velha = nome
            if idade < 18:
                qtd_mulheres_menos_18+=1

        elif idade < idade_mulher_mais_nova:
            idade_mulher_mais_nova = idade
            nome_mulher_mais_nova = nome
            if idade < 18:
                qtd_mulheres_menos_18+=1

        elif idade < 18:
            qtd_mulheres_menos_18 += 1

        media_idade += idade

    qtd_entrevistados += 1

    continua = input("\nDeseja ver mais dados de mais entrevistados? (S/N): ")

    if continua.upper() in ["S","SS", "SIM"]:
        quer_continuar = True
    else:
        quer_continuar = False

media_idade = media_idade / qtd_entrevistados

print(f"A pessoa mais velha se chama '{nome_pessoa_mais_velha}' e tem {maior_idade} anos")
print(f"A mulher mais jovem se chama '{nome_mulher_mais_nova}' e tem {idade_mulher_mais_nova} anos")
print(f"A média de idade do grupo é de: {media_idade} anos")
print(f"{qtd_homens_mais_30_anos} homen(s) tem mais de 30 anos")
print(f"{qtd_mulheres_menos_18} mulhere(s) tem menos de 18 anos")
