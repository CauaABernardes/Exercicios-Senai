salario_atual = float(input("Digite o salário atual do funcionário: "))
sexo = input("Digite o sexo do funcionário\n('M' para masculino e 'F' para feminino): ")
anos_empresa = int(input("Digite há quantos anos o funcionário está na empresa: "))

if sexo == "F" and salario_atual > 0 and anos_empresa >= 0:
    salario_novo = salario_atual
    if anos_empresa < 15:
        salario_novo += salario_atual * 0.05
    elif anos_empresa <= 20:
        salario_novo += salario_atual * 0.12
    else:
        salario_novo += salario_atual * 0.23
    print(f"O salário da funcionária após o reajuste é de: R${salario_novo}")
elif sexo == "M" and salario_atual > 0 and anos_empresa >= 0:
    salario_novo = salario_atual
    if anos_empresa < 20:
        salario_novo += salario_atual * 0.03
    elif anos_empresa <= 30:
        salario_novo += salario_atual * 0.13
    else:
        salario_novo += salario_atual * 0.25
    print(f"O salário do funcionário após o reajuste é de: R${salario_novo}")
else:
    print("Informações inválidas")