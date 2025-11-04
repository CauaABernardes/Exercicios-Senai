import random as rd
import os

coordenada_tesouro = rd.randint(1,10)

achou_tesouro = False

while not achou_tesouro:
    resposta = int(input("Qual o número que você acha que o tesouro está escondido?: "))

    if resposta != coordenada_tesouro:
        if resposta < coordenada_tesouro:
            print("Mais à direita\n")
        else:
            print("Mais à esquerda\n")
    
    else:
        os.system('cls')
        print("Você achou o tesouro!!!!")
        achou_tesouro = True
