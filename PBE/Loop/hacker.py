import random as rd

tentativas = 0

def definirSenha():
    global senha
    senha = ""

    for i in range(4):
        senha += rd.choice("0123456789")

def verificarSenha(senha_hacker):
    global acertou
    acertou = False
    qtd_digitos_corretos = 0
    
    if len(senha_hacker) != len(senha):
        print("A senha deve conter exatamente 4 dígitos numéricos")
        return
    
    for n in range(len(senha)):
        if senha_hacker[n] == senha[n]:
            qtd_digitos_corretos += 1
    
    print(f"Você acertou {qtd_digitos_corretos} de 4 digitos")

    if qtd_digitos_corretos == 4:
        acertou = True

def jogar():

    definirSenha()
    
    for i in range(1, 1001):
        global tentativas
        tentativas = i

        tentativa_senha = input("Digite qual você acha que é a senha de 4 dígitos: ")

        verificarSenha(tentativa_senha)

        if acertou:
            print(f"Você acertou a senha: {senha} em {tentativas} tentativas")
            break
        
    if tentativas == 1000:
        print("Você perdeu e gastou todas as sua tentativas!")
    

jogar()