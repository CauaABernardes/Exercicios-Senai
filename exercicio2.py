print("+==================================+")
print("|        Cofre  do  Marquin        |")
print("|==================================|")
print("|            Como  Jogar:          |")
print("|----------------------------------|")
print("| 1 - Decida quem jogará primeiro  |")
print("|                                  |")
print("| 2 - O primeiro deve escolher du- |\n| as senhas, sendo uma palavra e   |\n| outra sendo um número            |")
print("|                                  |")
print("| 3 - Após o primeiro escolher o   |\n| segundo deve adivinhar as senhas |")
print("|                                  |")
print("| 4 - Se o segundo acertar ele ga- |\n| nha e o cofre abre, senão ele    |\n| perde e o cofre fica fechado     |")
print("+==================================+")

CHAVE_PALAVRA = input("\nDigite a sua chave palavra: ")
CHAVE_NUMERO = int(input("Digite a sua chave número: "))

print("\n"*100)

print("Jogador 2:\nAdivinhe as chaves inseridas pelo Jogador 1")

chave_palavra_jogador2 = input("\nAdivinhe a chave palavra: ")
chave_numero_jogador2 = int(input("Adivinhe a chave número: "))

if chave_palavra_jogador2 != CHAVE_PALAVRA or chave_numero_jogador2 != CHAVE_NUMERO:
    print("\nCofre fechado\nChave palavra ou chave número incorretas")

else:
    print("\nCofre aberto!\nParabéns você conseguiu")