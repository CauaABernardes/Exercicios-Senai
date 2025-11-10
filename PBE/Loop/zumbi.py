import random as rd
from time import sleep

municoes = 5
zumbis = 10

morreu_jogador = False

def matarZumbis():
    global zumbis, municoes

    zumbis_matados = rd.randint(0,3)

    municoes -=1
    zumbis -= zumbis_matados

    print(f"\nVocê atirou e matou {zumbis_matados} ZUMBIS, ainda restam {zumbis} ZUMBIS\n")

def resultado():
    global morreu_jogador

    if zumbis <= 0:
        morreu_jogador == False
        print("\nVocê sobreviveu!!!")
        print(f"Sobraram {municoes} munições")

    elif municoes == 0:
        morreu_jogador = True
        print("\nVocê morreu!!!")
        print(f"Sobraram {zumbis} ZUMBIS")
    
def jogar():
    for _ in range (5):
        sleep(1)
        matarZumbis()
        sleep(0.5)
        resultado()

        if morreu_jogador:
            break

jogar()