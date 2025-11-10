import os
import random as rd
from time import sleep
from tqdm import tqdm

while True:

    sleep(1)
    os.system('cls')

    print("+----------------------+")
    print("|                      |")
    print("|    Jogos do Killwan  |")
    print("|                      |")
    print("+--------OPÇÕES--------+")
    print("|                      |")
    print("| 1) ACHE O TESOURO    |")
    print("| 2) COMBATE O MONSTRO |")
    print("| 3) SENHA HACKER      |")
    print("| 4) CORRIDA DE ROBÔS  |")
    print("| 5) MATE OS ZUMBIS    |")
    print("| 0) SAIR              |")
    print("|                      |")
    print("+----------------------+")

    try:
        opcao = int(input("Digite a sua opção desejada: "))
        
        if opcao not in [0, 1, 2, 3, 4, 5]:
            print("Opção inválida")

        else:

            if opcao == 1:
                
                while True:
                    
                    print("+--------------------+")
                    print("|    ACHE O TESOURO  |")
                    print("+-----DIFICULDADE----+")
                    print("| 1) FÁCIL           |")
                    print("| 2) MÉDIO           |")
                    print("| 3) DIFÍCIL         |")
                    print("+--------------------+")

                    dificuldade = int(input("Escolha a dificuldade: "))

                    if dificuldade not in [1, 2, 3]:
                        print("Escolha uma dificuldade válida!")
                    else:
                        break
                

                print()

                for i in tqdm(range(100), colour = "green"):
                    sleep(0.02)

                if dificuldade == 1:

                    coordenada_tesouro = rd.randint(1,10)

                    achou_tesouro = False

                    print("\n\nO tesouro esta em uma posição entre 1 e 10\nConsegue adivinhar onde ele está???")

                    while not achou_tesouro:
                        resposta = int(input("Qual o número que você acha que o tesouro está escondido?: "))

                        if resposta != coordenada_tesouro:
                            if resposta < coordenada_tesouro:
                                print("Mais à direita\n")
                            else:
                                print("Mais à esquerda\n")
                        
                        else:
                            print("\nVocê achou o tesouro!!!!")
                            achou_tesouro = True
                    
                            input("\nAperte qualquer tecla para continuar...: ")

                elif dificuldade == 2:

                    coordenada_tesouro = rd.randint(1,100)

                    achou_tesouro = False

                    tentativas_tesouro = 10

                    print("\n\nO tesouro esta em uma posição entre 1 e 100\nConsegue adivinhar onde ele está???")

                    while tentativas_tesouro > 0:
                        if not achou_tesouro:

                            resposta = int(input("Qual o número que você acha que o tesouro está escondido?: "))

                            if resposta != coordenada_tesouro:
                                if resposta < coordenada_tesouro:
                                    print("Mais à direita\n")
                                    tentativas_tesouro-=1
                                else:
                                    print("Mais à esquerda\n")
                                    tentativas_tesouro-=1
                            
                            else:
                                print("\nVocê achou o tesouro!!!!")
                                achou_tesouro = True
                        
                                input("\nAperte qualquer tecla para continuar...: ")
                        else:
                            break
                    
                else:

                    coordenada_tesouro = rd.randint(1,1000000)

                    achou_tesouro = False

                    print("\n\nO tesouro esta em uma posição entre 1 e 1.000.000\nConsegue adivinhar onde ele está???")

                    while not achou_tesouro:
                        resposta = int(input("Qual o número que você acha que o tesouro está escondido?: "))

                        if resposta != coordenada_tesouro:
                            if resposta < coordenada_tesouro:
                                print("Mais à direita\n")
                            else:
                                print("Mais à esquerda\n")
                        
                        else:
                            print("\nVocê achou o tesouro!!!!")
                            achou_tesouro = True
                    
                            input("\nAperte qualquer tecla para continuar...: ")

            elif opcao == 2:

                while True:
                    
                    print("+--------------------+")
                    print("|  COMBATE O MONSTRO |")
                    print("+-----DIFICULDADE----+")
                    print("| 1) FÁCIL           |")
                    print("| 2) MÉDIO           |")
                    print("| 3) DIFÍCIL         |")
                    print("+--------------------+")

                    dificuldade = int(input("Escolha a dificuldade: "))

                    if dificuldade not in [1, 2, 3]:
                        print("Escolha uma dificuldade válida!")
                    else:
                        break

                print()

                for i in tqdm(range(100), colour = "green"):
                    sleep(0.02)

                if dificuldade == 1:

                    vida_jogador = 120
                    vida_monstro = 100
                    rodadas = 0

                    while vida_jogador > 0 and vida_monstro > 0:

                        print("\nJogador ataca monstro, PEW PEW!!!")
                        dano = rd.randint(10,25)
                        vida_monstro -= dano
                        print(f"Vida atual do Monstro: {vida_monstro}")

                        for i in tqdm(range(100), colour = "blue"):
                            sleep(0.03)

                        if vida_monstro >= 0:
                            print("\nMonstro ataca jogador, Raw Raw!!!")
                            dano = rd.randint(5,25)
                            vida_jogador -= dano
                            print(f"Vida atual do Jogador: {vida_jogador}")

                            for i in tqdm(range(100), colour = "red"):
                                sleep(0.03)

                        rodadas += 1

                    print()

                    for i in tqdm(range(100), colour = "yellow"):
                        sleep(0.06)
                    
                    if vida_jogador > 0 and vida_monstro <=0:
                        print(f"\nO vencedor foi o Jogador, restando {vida_jogador} de vida\nA batalha durou {rodadas} rodadas")
                        input("\nAperte qualquer tecla para continuar...: ")

                    elif vida_jogador <= 0 and vida_monstro > 0:
                        print(f"\nO vencedor foi o Monstro, restando {vida_monstro} de vida\nA batalha durou {rodadas} rodadas")
                        print("GAME OVER!!!!")
                        input("\nAperte qualquer tecla para continuar...: ")

                    else:
                        print("\nAmbos morreram!")

                        input("\nAperte qualquer tecla para continuar...: ")

                elif dificuldade == 2:

                    vida_jogador = 100
                    vida_monstro = 100
                    rodadas = 0

                    while vida_jogador > 0 and vida_monstro > 0:

                        print("\nJogador ataca monstro, PEW PEW!!!")
                        dano = rd.randint(10,25)
                        vida_monstro -= dano
                        print(f"Vida atual do Monstro: {vida_monstro}")

                        for i in tqdm(range(100), colour = "blue"):
                            sleep(0.03)

                        if vida_monstro >= 0:
                            print("\nMonstro ataca jogador, Raw Raw!!!")
                            dano = rd.randint(5,30)
                            vida_jogador -= dano
                            print(f"Vida atual do Jogador: {vida_jogador}")

                            for i in tqdm(range(100), colour = "red"):
                                sleep(0.03)

                        rodadas += 1

                    print()

                    for i in tqdm(range(100), colour = "yellow"):
                        sleep(0.06)
                    
                    if vida_jogador > 0 and vida_monstro <=0:
                        print(f"\nO vencedor foi o Jogador, restando {vida_jogador} de vida\nA batalha durou {rodadas} rodadas")
                        input("\nAperte qualquer tecla para continuar...: ")

                    elif vida_jogador <= 0 and vida_monstro > 0:
                        print(f"\nO vencedor foi o Monstro, restando {vida_monstro} de vida\nA batalha durou {rodadas} rodadas")
                        print("GAME OVER!!!!")
                        input("\nAperte qualquer tecla para continuar...: ")

                    else:
                        print("\nAmbos morreram!")

                        input("\nAperte qualquer tecla para continuar...: ")

                else:

                    vida_jogador = 110
                    vida_monstro = 120
                    rodadas = 0

                    while vida_jogador > 0 and vida_monstro > 0:

                        print("\nJogador ataca monstro, PEW PEW!!!")
                        dano = rd.randint(15,30)
                        vida_monstro -= dano
                        print(f"Vida atual do Monstro: {vida_monstro}")

                        for i in tqdm(range(100), colour = "blue"):
                            sleep(0.03)

                        if vida_monstro >= 0:
                            print("\nMonstro ataca jogador, Raw Raw!!!")
                            dano = rd.randint(15,35)
                            vida_jogador -= dano
                            print(f"Vida atual do Jogador: {vida_jogador}")

                            for i in tqdm(range(100), colour = "red"):
                                sleep(0.03)

                        rodadas += 1

                    print()

                    for i in tqdm(range(100), colour = "yellow"):
                        sleep(0.06)
                    
                    if vida_jogador > 0 and vida_monstro <=0:
                        print(f"\nO vencedor foi o Jogador, restando {vida_jogador} de vida\nA batalha durou {rodadas} rodadas")
                        input("\nAperte qualquer tecla para continuar...: ")

                    elif vida_jogador <= 0 and vida_monstro > 0:
                        print(f"\nO vencedor foi o Monstro, restando {vida_monstro} de vida\nA batalha durou {rodadas} rodadas")
                        print("GAME OVER!!!!")
                        input("\nAperte qualquer tecla para continuar...: ")

                    else:
                        print("\nAmbos morreram!")

                        input("\nAperte qualquer tecla para continuar...: ")

            elif opcao == 3:

                while True:
                    
                    print("+--------------------+")
                    print("|     SENHA HACKER   |")
                    print("+-----DIFICULDADE----+")
                    print("| 1) FÁCIL           |")
                    print("| 2) MÉDIO           |")
                    print("| 3) DIFÍCIL         |")
                    print("+--------------------+")

                    dificuldade = int(input("Escolha a dificuldade: "))

                    if dificuldade not in [1, 2, 3]:
                        print("Escolha uma dificuldade válida!")
                    else:
                        break

                if dificuldade == 1:

                    acertou = False
                    tentativas = 0
                    senha = ""

                    print()

                    for i in tqdm(range(100), colour = "green"):
                        sleep(0.02)

                    for i in range(4):
                        senha += rd.choice("0123456789")

                    for i in range(1, 1001):

                        tentativas = i

                        tentativa_senha = input("Digite qual você acha que é a senha de 4 dígitos: ")

                        qtd_digitos_corretos = 0
                        
                        try:

                            if len(tentativa_senha) != len(senha):
                                print("A senha deve conter exatamente 4 dígitos numéricos")
                            
                            for n in range(len(senha)):
                                if tentativa_senha[n] == senha[n]:
                                    qtd_digitos_corretos += 1
                            
                            print(f"Você acertou {qtd_digitos_corretos} de 4 digitos")

                            if qtd_digitos_corretos == 4:
                                acertou = True

                            if acertou:
                                print(f"Você acertou a senha: {senha} em {tentativas} tentativas")
                                break
                        except:
                            pass
                    if tentativas == 1000:
                        print("Você perdeu e gastou todas as sua tentativas!")

                    input("\nAperte qualquer tecla para continuar...: ")
                
                elif dificuldade == 2:

                    acertou = False
                    tentativas = 0
                    senha = ""

                    print()

                    for i in tqdm(range(100), colour = "green"):
                        sleep(0.02)

                    for i in range(5):
                        senha += rd.choice("0123456789")

                    for i in range(1, 101):

                        tentativas = i

                        tentativa_senha = input("Digite qual você acha que é a senha de 5 dígitos: ")

                        qtd_digitos_corretos = 0
                        
                        try:

                            if len(tentativa_senha) != len(senha):
                                print("A senha deve conter exatamente 5 dígitos numéricos")
                            
                            for n in range(len(senha)):
                                if tentativa_senha[n] == senha[n]:
                                    qtd_digitos_corretos += 1
                            
                            print(f"Você acertou {qtd_digitos_corretos} de 5 digitos")

                            if qtd_digitos_corretos == 5:
                                acertou = True

                            if acertou:
                                print(f"Você acertou a senha: {senha} em {tentativas} tentativas")
                                break
                        except:
                            pass
                    if tentativas == 100:
                        print("Você perdeu e gastou todas as sua tentativas!")

                    input("\nAperte qualquer tecla para continuar...: ")

                else:

                    acertou = False
                    tentativas = 0
                    senha = ""

                    print()

                    for i in tqdm(range(100), colour = "green"):
                        sleep(0.02)

                    for i in range(8):
                        senha += rd.choice("0123456789abcde#!")

                    print("\nNeste modo de jogo pode conter também as letras: a, b, c, d, e, #, !")

                    for i in range(1, 101):

                        tentativas = i

                        tentativa_senha = input("Digite qual você acha que é a senha de 8 dígitos: ")

                        qtd_digitos_corretos = 0
                        
                        try:

                            if len(tentativa_senha) != len(senha):
                                print("A senha deve conter exatamente 8 dígitos numéricos")
                            
                            for n in range(len(senha)):
                                if tentativa_senha[n] == senha[n]:
                                    qtd_digitos_corretos += 1
                            
                            print(f"Você acertou {qtd_digitos_corretos} de 8 digitos")

                            if qtd_digitos_corretos == 8:
                                acertou = True

                            if acertou:
                                print(f"Você acertou a senha: {senha} em {tentativas} tentativas")
                                break
                        except:
                            pass
                    if tentativas == 100:
                        print("Você perdeu e gastou todas as sua tentativas!")

                    input("\nAperte qualquer tecla para continuar...: ")

            elif opcao == 4:

                passos_robo_1 = 0
                passos_robo_2 = 0

                ganhou_robo_1 = False
                ganhou_robo_2 = False 

                print()

                for i in tqdm(range(100), colour = "green"):
                    sleep(0.02)

                while True:
                    qtd_passos = rd.randint(1,3)
                    passos_robo_1 += qtd_passos

                    qtd_passos = rd.randint(1,3)
                    passos_robo_2 += qtd_passos

                    sleep(0.2)

                    if passos_robo_1 >= 20:
                        ganhou_robo_1 = True

                    if passos_robo_2 >= 20:
                        ganhou_robo_2 = True

                    print("===================+")
                    print("   Trecho Robô R1  |")
                    print("#"*passos_robo_1)
                    print("===================+")
                    print("#"*passos_robo_2)
                    print("   Trecho Robô R2  |")
                    print("===================+")

                    sleep(1)

                    if ganhou_robo_1 and ganhou_robo_2:
                        if passos_robo_1 > passos_robo_2:
                            print("O R1 ganhou!!!")
                            input("\nAperte qualquer tecla para continuar...: ")
                            break
                        elif passos_robo_2 > passos_robo_1:
                            print("O R2 ganhou!!!")
                            input("\nAperte qualquer tecla para continuar...: ")
                            break
                        else:
                            print("Empate técnico!!!")
                            input("\nAperte qualquer tecla para continuar...: ")
                            break
                    elif ganhou_robo_1:
                        print("O R1 ganhou!!!")
                        input("\nAperte qualquer tecla para continuar...: ")
                        break
                    elif ganhou_robo_2:
                        print("O R2 ganhou!!!")
                        input("\nAperte qualquer tecla para continuar...: ")
                        break
                        
                    os.system('cls')

            elif opcao == 5:

                while True:
                    
                    print("+--------------------+")
                    print("|    MATE OS ZUMBIS  |")
                    print("+-----DIFICULDADE----+")
                    print("| 1) FÁCIL           |")
                    print("| 2) MÉDIO           |")
                    print("| 3) DIFÍCIL         |")
                    print("+--------------------+")

                    dificuldade = int(input("Escolha a dificuldade: "))

                    if dificuldade not in [1, 2, 3]:
                        print("Escolha uma dificuldade válida!")
                    else:
                        break

                print()

                for i in tqdm(range(100), colour = "green"):
                    sleep(0.02)
                
                if dificuldade == 1:
                    municoes = 5
                    zumbis = 8

                    morreu_jogador = False

                    for _ in range(5):
                        sleep(0.5)
                        zumbis_matados = rd.randint(0,3)

                        municoes -=1
                        zumbis -= zumbis_matados

                        print(f"\nVocê atirou e matou {zumbis_matados} ZUMBIS, ainda restam {zumbis} ZUMBIS\n")
                        sleep(0.5)
                        if zumbis <= 0:
                            morreu_jogador == False
                            print("\nVocê sobreviveu!!!")
                            print(f"Sobraram {municoes} munições")
        
                        elif municoes == 0:
                            morreu_jogador = True
                            print("\nVocê morreu!!!")
                            print(f"Sobraram {zumbis} ZUMBIS")

                        sleep(0.5)

                        if morreu_jogador:
                            break
                    input("\nAperte qualquer tecla para continuar...: ")

                if dificuldade == 2:
                    municoes = 4
                    zumbis = 10

                    morreu_jogador = False

                    for _ in range(5):
                        sleep(0.5)
                        zumbis_matados = rd.randint(0,3)

                        municoes -=1
                        zumbis -= zumbis_matados

                        print(f"\nVocê atirou e matou {zumbis_matados} ZUMBIS, ainda restam {zumbis} ZUMBIS\n")
                        sleep(0.5)
                        if zumbis <= 0:
                            morreu_jogador == False
                            print("\nVocê sobreviveu!!!")
                            print(f"Sobraram {municoes} munições")
        
                        elif municoes == 0:
                            morreu_jogador = True
                            print("\nVocê morreu!!!")
                            print(f"Sobraram {zumbis} ZUMBIS")

                        sleep(0.5)

                        if morreu_jogador:
                            break
                    input("\nAperte qualquer tecla para continuar...: ")
                
                else:
                    municoes = 7
                    zumbis = 20

                    morreu_jogador = False
                    arma_travou = False

                    for _ in range(7):
                        sleep(0.5)
                        zumbis_matados = rd.randint(0,5)

                        municoes -=1

                        arma_atirou = rd.randint(0,1)

                        if arma_atirou == 0:
                            arma_travou = True
                        else:
                            arma_travou = False
                        
                        if not arma_travou:

                            zumbis -= zumbis_matados

                            print(f"\nVocê atirou e matou {zumbis_matados} ZUMBIS, ainda restam {zumbis} ZUMBIS\n")
                            sleep(0.5)
                            if zumbis <= 0:
                                morreu_jogador == False
                                print("\nVocê sobreviveu!!!")
                                print(f"Sobraram {municoes} munições")
            
                            elif municoes == 0:
                                morreu_jogador = True
                                print("\nVocê morreu!!!")
                                print(f"Sobraram {zumbis} ZUMBIS")

                            sleep(0.5)

                            if morreu_jogador:
                                break
                        else:
                            print("A arma emperrou e gastou uma munição!")
                            sleep(1)
                            if zumbis <= 0:
                                morreu_jogador == False
                                print("\nVocê sobreviveu!!!")
                                print(f"Sobraram {municoes} munições")
            
                            elif municoes == 0:
                                morreu_jogador = True
                                print("\nVocê morreu!!!")
                                print(f"Sobraram {zumbis} ZUMBIS")

                            sleep(0.5)

                            if morreu_jogador:
                                break
                            
                    input("\nAperte qualquer tecla para continuar...: ")

            elif opcao == 0:
                print("\nObrigado por utilizar nosso arcade!")
                break
    except:
        print("Digite apenas opções válidas!")