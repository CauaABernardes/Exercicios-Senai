import random as rd

tentativas = 0

senha = rd.randint(1000, 9999)
digitos_senha = [int(digito) for digito in str(senha)]

def perguntarSenha():
    global tentativas
    while True:
        digitos_jogador = input("Qual você acha que é a senha: ")

        if not digitos_jogador.isdigit() or len(digitos_jogador) != 4:
            print("Digite uma senha com 4 números!")
            continue

        tentativas += 1
        digitos_jogador = [int(digito) for digito in digitos_jogador]

        if compararSenhas(digitos_senha, digitos_jogador):
            print(f"Parabéns! Você acertou a senha {senha} em {tentativas} tentativas!")
            break

def compararSenhas(senha_padrao, senha_jogador):
    digitos_corretos = sum(1 for d in senha_jogador if d in senha_padrao)
    print(f"Você acertou {digitos_corretos} de 4 dígitos.")
    return senha_jogador == senha_padrao

perguntarSenha()
