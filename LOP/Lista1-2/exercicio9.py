ano_nascimento = int(input("Digite seu ano de nascimento: "))

anos_alistamento = 2025 - (ano_nascimento + 18)

if anos_alistamento < 0:
    anos_alistamento *= -1

if ano_nascimento < 2007:
    print(f"Já se passaram {anos_alistamento} anos do seu alistamento")
elif ano_nascimento > 2007:
    print(f"Faltam {anos_alistamento} anos para o seu alistamento")
else:
    print("Você está no processo de alistamento")