media_salarial = 0
media_de_filhos = 0
qtd_pessoas_salario_menor_150 = 0
qtd_entrevistados = 0

maior_salario = float(input("Digite o seu salário: "))
salario_digitado = maior_salario

while salario_digitado >= 0:
    qtd_filhos = int(input("Digite quantos filhos você tem: "))

    qtd_entrevistados += 1

    if salario_digitado < 150:
        qtd_pessoas_salario_menor_150 += 1

    if salario_digitado > maior_salario:
        maior_salario = salario_digitado

    media_salarial += salario_digitado
    media_de_filhos += qtd_filhos

    salario_digitado = float(input("Digite o seu salário: "))

media_de_filhos = media_de_filhos/qtd_entrevistados
media_salarial = media_salarial/qtd_entrevistados

porcentagem_menor_150 = (qtd_pessoas_salario_menor_150 / qtd_entrevistados) * 100

print(f"A média salarial da população é de: R${media_salarial:.2f} por pessoa")
print(f"A média de filhos da população é de: {media_de_filhos:.2f} por pessoa")
print(f"O maior salário é de: R${maior_salario}")
print(f"O percentual de pessoas que ganham menos de R$150 é de: {porcentagem_menor_150:.2f}% das pessoas")
