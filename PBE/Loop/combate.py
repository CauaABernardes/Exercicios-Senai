import random as rd
from tqdm import tqdm
from time import sleep

vida_jogador = 100
vida_monstro = 100
rodadas = 0

def ataqueJogador():
    global  vida_monstro
    print("Jogador ataca monstro, PEW PEW!!!")
    dano = rd.randint(10,30)
    vida_monstro -= dano
    print(f"Vida atual do Monstro: {vida_monstro}")

    if vida_monstro <= 0:
        return
    else:
        tempo()
        ataqueMonstro()

def ataqueMonstro():
    global vida_jogador
    print("Monstro ataca jogador, Raw Raw!!!")
    dano = rd.randint(5,25)
    vida_jogador -= dano
    print(f"Vida atual do Jogador: {vida_jogador}")

def tempo():
    for i in tqdm(range(100), colour = "green"):
        sleep(0.02)

def definirGanhador():
    if vida_jogador > 0 and vida_monstro <=0:
        print(f"O vencedor foi o Jogador, restando {vida_jogador} de vida\nA batalha durou {rodadas} rodadas")

    elif vida_jogador <= 0 and vida_monstro > 0:
        print(f"O vencedor foi o Monstro, restando {vida_monstro} de vida\nA batalha durou {rodadas} rodadas")
        print("GAME OVER!!!!")

    else:
        print("Ambos morreram!")

while vida_jogador > 0 and vida_monstro > 0:
    ataqueJogador()
    tempo()
    rodadas+=1

definirGanhador()