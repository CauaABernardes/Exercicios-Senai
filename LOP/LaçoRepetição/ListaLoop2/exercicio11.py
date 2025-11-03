parou = False

SALARIO_MIN = 1804
PORCENTAGEM_CLASSE_B = 0.03
PORCENTAGEM_CLASSE_C = 0.05

total_pecas_fabricadas = 0
total_folha_pagamento = 0

funcionarios = []

qtd_funcionarios_classe_A_masc = 0
qtd_funcionarios_classe_A_femin = 0

media_pecas_classe_A_masc = 0
media_pecas_classe_A_femin = 0

qtd_funcionarios_classe_B_masc = 0
qtd_funcionarios_classe_B_femin = 0

media_pecas_classe_B_masc = 0
media_pecas_classe_B_femin = 0

qtd_funcionarios_classe_C_masc = 0
qtd_funcionarios_classe_C_femin = 0

media_pecas_classe_C_masc = 0
media_pecas_classe_C_femin = 0

num_funcionario_maior_salario = 0
maior_salario = 0

while not parou:
    num_operario = int(input("Digite o número de identificação do(a) funcionário(a): "))
    qtd_pecas_fabricas_no_mes = int(input("Digite quantas peças o(a) funcionário(a) fabricou no mês: "))
    sexo_do_funcionario = int(input("Digite o sexo do(a) funcionário(a)\n(0 para masculino/1 para feminino): "))

    if num_operario == 0 and qtd_pecas_fabricas_no_mes == 0 and sexo_do_funcionario == 0:
        parou = True

    else:
        if qtd_pecas_fabricas_no_mes <= 30:
            salario = SALARIO_MIN
            funcionario = {"Identificação": num_operario, "Fabricação de Peças": qtd_pecas_fabricas_no_mes,
                           "Salário": salario,"Sexo": sexo_do_funcionario, "Classe": "A"}

        elif qtd_pecas_fabricas_no_mes > 30 and qtd_pecas_fabricas_no_mes <= 35:
            pecas_a_mais = qtd_pecas_fabricas_no_mes - 30
            salario = SALARIO_MIN + (SALARIO_MIN * (PORCENTAGEM_CLASSE_B * pecas_a_mais))
            funcionario = {"Identificação": num_operario, "Fabricação de Peças": qtd_pecas_fabricas_no_mes,
                           "Salário": salario,"Sexo": sexo_do_funcionario, "Classe": "B"}

        else:
            pecas_a_mais = qtd_pecas_fabricas_no_mes - 30
            salario = SALARIO_MIN + (SALARIO_MIN * (PORCENTAGEM_CLASSE_C * pecas_a_mais))
            funcionario = {"Identificação": num_operario, "Fabricação de Peças": qtd_pecas_fabricas_no_mes,
                           "Salário": salario, "Sexo": sexo_do_funcionario, "Classe": "C"}

        total_pecas_fabricadas += qtd_pecas_fabricas_no_mes
        total_folha_pagamento += salario

        if salario > maior_salario:
            maior_salario = salario
            num_funcionario_maior_salario = num_operario

        funcionarios.append(funcionario)

    print()

print(f"A fábrica produziu ao total {total_pecas_fabricadas} peças no mês\nTendo um total na folha de pagamento de: R${total_folha_pagamento}")

print(f"O maior salário foi do(a) operário(a) {num_funcionario_maior_salario:.2f}")

print("Salário de cada operário(a):")

for operario in funcionarios:
    if operario["Sexo"] == 0:
        print(f"O Operário {operario["Identificação"]} fabricou {operario["Fabricação de Peças"]} peças"
              f", seu salário é de: R${operario["Salário"]:.2f}")

        if operario["Classe"] == "A":
            qtd_funcionarios_classe_A_masc += 1
            media_pecas_classe_A_masc += operario["Fabricação de Peças"]

        elif operario["Classe"] == "B":
            qtd_funcionarios_classe_B_masc += 1
            media_pecas_classe_B_masc += operario["Fabricação de Peças"]

        else:
            qtd_funcionarios_classe_C_masc += 1
            media_pecas_classe_C_masc += operario["Fabricação de Peças"]

    else:
        print(f"A Operária {operario["Identificação"]} fabricou {operario["Fabricação de Peças"]} peças"
              f", seu salário é de: R${operario["Salário"]:.2f}")

        if operario["Classe"] == "A":
            qtd_funcionarios_classe_A_femin += 1
            media_pecas_classe_A_femin += operario["Fabricação de Peças"]

        elif operario["Classe"] == "B":
            qtd_funcionarios_classe_B_femin+= 1
            media_pecas_classe_B_femin += operario["Fabricação de Peças"]

        else:
            qtd_funcionarios_classe_C_femin += 1
            media_pecas_classe_C_femin += operario["Fabricação de Peças"]

media_pecas_classe_A_masc = media_pecas_classe_A_masc // qtd_funcionarios_classe_A_masc
media_pecas_classe_A_femin = media_pecas_classe_A_femin // qtd_funcionarios_classe_A_femin

media_pecas_classe_B_masc = media_pecas_classe_B_masc // qtd_funcionarios_classe_B_masc
media_pecas_classe_B_femin = media_pecas_classe_B_femin // qtd_funcionarios_classe_B_femin

media_pecas_classe_C_masc = media_pecas_classe_C_masc // qtd_funcionarios_classe_C_masc
media_pecas_classe_C_femin = media_pecas_classe_C_femin // qtd_funcionarios_classe_C_femin

print("Média de peças por classe e sexo:")
print("\nHomens da classe 'A':")
print(f"Média de peças fabricadas por homem: {media_pecas_classe_A_masc} por homem")
print("\nMulheres da classe 'A':")
print(f"Média de peças fabricadas por mulher: {media_pecas_classe_A_femin} por mulher")
print("\n\nHomens da classe 'B':")
print(f"Média de peças fabricadas por homem: {media_pecas_classe_B_masc} por homem")
print("\nMulheres da classe 'B':")
print(f"Média de peças fabricadas por mulher: {media_pecas_classe_B_femin} por mulher")
print("\n\nHomens da classe 'C':")
print(f"Média de peças fabricadas por homem: {media_pecas_classe_C_masc} por homem")
print("\nMulheres da classe 'C':")
print(f"Média de peças fabricadas por mulher: {media_pecas_classe_C_femin} por mulher")