salario_fixo = float(input("Digite o seu salário fixo: "))
valor_vendas = float(input("Digite quanto foi o valor de vendas que você efetuou no total: "))

if valor_vendas <= 1500:
    acrescimo = valor_vendas * 0.03
else:
    acrescimo = valor_vendas * 0.05

if salario_fixo <= 0:
    print("Salário inválido")

else:
    salario_total = salario_fixo + acrescimo

    print(f"O seu salário após a sua comissão de vendas é de: R$ {salario_total}")
