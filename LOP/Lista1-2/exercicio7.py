ano_nascimento = int(input("Digie o ano que você nasceu: "))

if ano_nascimento > 2025:
    print("Ano inválido")
elif ano_nascimento <= 2009:
    print("Você pode votar")
else:
    print("Você não pode votar")