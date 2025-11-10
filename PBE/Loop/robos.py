import random as rd
import os
from time import sleep


passos_robo_1 = 0
passos_robo_2 = 0

ganhou_robo_1 = False
ganhou_robo_2 = False 

def passoRobo(num_robo):
    global passos_robo_1, passos_robo_2, ganhou_robo_1, ganhou_robo_2

    if num_robo == 1:
        qtd_passos = rd.randint(1,3)
        passos_robo_1 += qtd_passos

        if passos_robo_1 >= 20:
            ganhou_robo_1 = True
    else:
        qtd_passos = rd.randint(1,3)
        passos_robo_2 += qtd_passos

        if passos_robo_2 >= 20:
            ganhou_robo_2 = True

def limparTela():
    sleep(2)
    os.system("cls")


def mostrarPassos():
    print("===================+")
    print("   Trecho Robô R1  |")
    print("#"*passos_robo_1)
    print("===================+")
    print("#"*passos_robo_2)
    print("   Trecho Robô R2  |")
    print("===================+")

def jogar():
    while True:
        limparTela()
        sleep(0.5)
        passoRobo(1)
        passoRobo(2)
        sleep(0.2)
        mostrarPassos()

        if ganhou_robo_1:
            print("O R1 ganhou!!!")
            break
        elif ganhou_robo_2:
            print("O R2 ganhou!!!")
            break
        elif ganhou_robo_1 and ganhou_robo_2:
            if passos_robo_1 > passos_robo_2:
                print("O R1 ganhou!!!")
                break
            elif passos_robo_2 > passos_robo_1:
                print("O R2 ganhou!!!")
                break
            else:
                print("Empate técnico!!!")
                break
        
jogar()