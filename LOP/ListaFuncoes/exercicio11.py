parou = False

SALARIO_MIN = 1804
PORCENTAGEM_CLASSE_B = 0.03
PORCENTAGEM_CLASSE_C = 0.05

total_pecas_fabricadas = 0
total_folha_pagamento = 0

funcionarios = []

funcionarios_masc_classe_A = 0
funcionarios_femim_classe_A = 0

funcionarios_masc_classe_B = 0
funcionarios_femim_classe_B = 0

funcionarios_masc_classe_C = 0
funcionarios_femim_classe_C = 0

pecas_classe_A_masc = 0
pecas_classe_A_femin = 0

pecas_classe_B_masc = 0
pecas_classe_B_femin = 0

pecas_classe_C_masc = 0
pecas_classe_C_femin = 0

num_funcionario_maior_salario = 0
maior_salario = 0

def media_classe_por_sexo(qtd_func_classe_sexo, qtd_pecas_classe_sexo, classe, sexo):
    if sexo == 0:
        media = qtd_pecas_classe_sexo / qtd_func_classe_sexo
        return f"Os homens da classe {classe} fizeram em média: {media:.2f} peças!"
    else:
        media = qtd_pecas_classe_sexo / qtd_func_classe_sexo
        return f"As mulheres da classe {classe} fizeram em média: {media:.2f} peças!"

while not parou:
    num_operario = int(input("\nDigite o número de identificação do(a) funcionário(a): "))
    qtd_pecas_fabricas_no_mes = int(input("Digite quantas peças o(a) funcionário(a) fabricou no mês: "))
    sexo_do_funcionario = int(input("Digite o sexo do(a) funcionário(a)\n(0 para masculino/1 para feminino): "))

    if num_operario == 0 and qtd_pecas_fabricas_no_mes == 0 and sexo_do_funcionario == 0:
        parou = True
    else:
        if qtd_pecas_fabricas_no_mes <= 30:
            salario = SALARIO_MIN
            funcionario = {"Identificação": num_operario, "Fabricação de Peças": qtd_pecas_fabricas_no_mes, "Salário": salario,"Sexo": sexo_do_funcionario, "Classe": "A"}
            if funcionario["Sexo"] == 0:
                funcionarios_masc_classe_A += 1
                pecas_classe_A_masc += funcionario["Fabricação de Peças"]
            else:
                funcionarios_femim_classe_A += 1
                pecas_classe_A_femin += funcionario["Fabricação de Peças"]

        elif qtd_pecas_fabricas_no_mes > 30 and qtd_pecas_fabricas_no_mes <= 35:
            pecas_a_mais = qtd_pecas_fabricas_no_mes - 30
            salario = SALARIO_MIN + (SALARIO_MIN * (PORCENTAGEM_CLASSE_B * pecas_a_mais))
            funcionario = {"Identificação": num_operario, "Fabricação de Peças": qtd_pecas_fabricas_no_mes, "Salário": salario,"Sexo": sexo_do_funcionario, "Classe": "B"}
            if funcionario["Sexo"] == 0:
                funcionarios_masc_classe_B += 1
                pecas_classe_B_masc += funcionario["Fabricação de Peças"]
            else:
                funcionarios_femim_classe_B += 1
                pecas_classe_B_femin += funcionario["Fabricação de Peças"]

        else:
            pecas_a_mais = qtd_pecas_fabricas_no_mes - 30
            salario = SALARIO_MIN + (SALARIO_MIN * (PORCENTAGEM_CLASSE_C * pecas_a_mais))
            funcionario = {"Identificação": num_operario, "Fabricação de Peças": qtd_pecas_fabricas_no_mes, "Salário": salario, "Sexo": sexo_do_funcionario, "Classe": "C"}
            if funcionario["Sexo"] == 0:
                funcionarios_masc_classe_C += 1
                pecas_classe_C_masc += funcionario["Fabricação de Peças"]
            else:
                funcionarios_femim_classe_C += 1
                pecas_classe_C_femin += funcionario["Fabricação de Peças"]


        total_pecas_fabricadas += qtd_pecas_fabricas_no_mes
        total_folha_pagamento += salario

        if salario > maior_salario:
            maior_salario = salario
            num_funcionario_maior_salario = num_operario

        funcionarios.append(funcionario)

print(f"\nA fábrica produziu ao total {total_pecas_fabricadas} peças no mês\nTendo um total na folha de pagamento de: R${total_folha_pagamento:.2f}")

print(f"\nO maior salário foi do(a) operário(a) {num_funcionario_maior_salario:.2f}")

print("\nSalário de cada operário(a):\n")

for operario in funcionarios:
    if operario["Sexo"] == 0:
        print(f"O Operário {operario["Identificação"]} fabricou {operario["Fabricação de Peças"]} peças, seu salário é de: R${operario["Salário"]:.2f}")
    else:
        print(f"A Operária {operario["Identificação"]} fabricou {operario["Fabricação de Peças"]} peças, seu salário é de: R${operario["Salário"]:.2f}")

print("\nMédia de peças por classe e sexo:")
print(media_classe_por_sexo(funcionarios_masc_classe_A, pecas_classe_A_masc, "A", 0))
print(media_classe_por_sexo(funcionarios_femim_classe_A, pecas_classe_A_femin, "A", 1))
print(media_classe_por_sexo(funcionarios_masc_classe_B, pecas_classe_B_masc, "B", 0))
print(media_classe_por_sexo(funcionarios_femim_classe_B, pecas_classe_B_femin, "B", 1))
print(media_classe_por_sexo(funcionarios_masc_classe_C, pecas_classe_C_masc, "C", 0))
print(media_classe_por_sexo(funcionarios_femim_classe_C, pecas_classe_C_femin, "C", 1))