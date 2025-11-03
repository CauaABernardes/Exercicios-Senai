quer_continuar = True
salario_total_homens = 0
salario_total_mulheres = 0
qtd_homens = 0
qtd_mulheres = 0

while quer_continuar:
    sexo = input("Qual é o sexo do(a) funcionário(a) (M/F): ")
    if sexo.upper() in ["M", "MASCULINO", "HOMEM"]:
       salario = float(input("Digite o salário do colaborador: R$"))
       salario_total_homens += salario
       qtd_homens += 1
    elif sexo.upper() in ["F", "FEMININO", "MULHER"]:
        salario = float(input("Digite o salário da colaboradora: R$"))
        salario_total_mulheres += salario
        qtd_mulheres += 1

    continua = input("\nDeseja ver mais dados de mais funcionários? (S/N): ")

    if continua.upper() in ["S","SS", "SIM"]:
        quer_continuar = True
    else:
        quer_continuar = False

print(f"O salário total dos {qtd_homens} homens lidos é de: R${salario_total_homens}")
print(f"O salário total das {qtd_mulheres} mulheres lidas é de: R${salario_total_mulheres}")
