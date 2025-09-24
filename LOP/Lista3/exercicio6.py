CODIGO_SISTEMA = 1234
SENHA_SISTEMA = 9999

codigo_usuario = int(input("Digite o código de usuário para acessar o sistema: "))

if codigo_usuario != CODIGO_SISTEMA:
    print("Usuário Inválido!")
else:
    senha_usuario = int(input(f"Digite a senha do usuário {CODIGO_SISTEMA} para entrar: "))

    if senha_usuario != SENHA_SISTEMA:
        print("Senha incorreta")
    else:
        print("Acesso permitido")