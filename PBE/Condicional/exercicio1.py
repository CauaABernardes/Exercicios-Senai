PEDRA = 1
TESOURA = 2
PAPEL = 3

print("+==================================+")
print("|        JoKenPo do Marquin        |")
print("|==================================|")
print("|            Como  Jogar:          |")
print("|----------------------------------|")
print("| 1 - Decida quem jogará primeiro  |")
print("| 2 - O primeiro deve escolher en- |\n| tre: Pedra, Papel ou Tesoura     |")
print("| 3 - Após o primeiro escolher o   |\n| segundo deve escolher também     |")
print("| 4 - Veja o resultado de quem ga- |\n| nhou                             |")
print("+==================================+")

print("\nJogador 1:\nEscolha 1 para Pedra\nEscolha 2 para Tesoura\nEscolha 3 para Papel")
resp_primeiro = int(input("\nDigite o que você quer jogar: "))

if resp_primeiro == PEDRA or resp_primeiro == TESOURA or resp_primeiro == PAPEL:

    print("\n"*100)

    print("Jogador 2:\nEscolha 1 para Pedra\nEscolha 2 para Tesoura\nEscolha 3 para Papel")
    resp_segundo = int(input("\nDigite o que você quer jogar: "))

    if resp_segundo == PEDRA or resp_segundo == TESOURA or resp_segundo == PAPEL:
        print()

        if resp_primeiro == PEDRA and resp_segundo == TESOURA:
            print("O jogador 1 é o vencedor!!!")
        elif resp_primeiro == TESOURA and resp_segundo == PAPEL:
            print("O jogador 1 é o vencedor!!!")
        elif resp_primeiro == PAPEL and resp_segundo == PEDRA:
            print("O jogador 1 é o vencedor!!!")
        elif resp_primeiro == TESOURA and resp_segundo == PEDRA:
            print("O jogador 2 é o vencedor!!!")
        elif resp_primeiro == PEDRA and resp_segundo == PAPEL:
            print("O jogador 2 é o vencedor!!!")
        elif resp_primeiro == PAPEL and resp_segundo == TESOURA:
            print("O jogador 2 é o vencedor!!!")
        else:
            print("Empate!")

    else:
        print("Opção inexistente!")

else:
    print("Opção inexistente!")