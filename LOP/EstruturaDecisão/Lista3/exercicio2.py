nome = input("Digite seu nome: ")
salario_atual = float(input("Digite o seu salário atual: "))
anos_empresa = int(input("Digite a quantos anos você trabalha na empresa: "))

if salario_atual <= 0:
    print("Salário inválido")

elif anos_empresa < 0:
    print("Anos na empresa inválidos")

else:
    if anos_empresa <= 3:
        salario_novo = salario_atual + (salario_atual * 0.03)
    elif anos_empresa <= 10:
        salario_novo = salario_atual + (salario_atual * 0.125)
    else:
        salario_novo = salario_atual + (salario_atual * 0.20)

    print(f"{nome} seu salário após o aumento é de: R$ {salario_novo}")