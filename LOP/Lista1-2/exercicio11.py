horas_trab = int(input("Digite quantas horas você trabalhou no mês: "))
salario_hora = float(input("Digite quanto é seu salário por hora: "))

if horas_trab < 0:
    print("Quantidade de horas trabalhadas inválidas")

elif horas_trab < 160:
    print("Você não irá receber reduzido")

else:
    horas_extra = horas_trab - 160
    salario_extra = (((salario_hora * 0.5) + salario_hora) * horas_extra)

    salario_total = (salario_hora * 160) + salario_extra

    print(f"O seu salário do mês é : R${salario_total}")