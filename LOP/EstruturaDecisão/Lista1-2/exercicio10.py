hora_inicio = int(input("Digite a hora que o jogo começou: "))
hora_fim = int(input("Digite a hora que o jogo terminou: "))

duracao_jogo = hora_fim - hora_inicio

if hora_inicio > 24 or hora_fim > 24:
    print("Hora inválida")

elif duracao_jogo == 0:
    print("O jogo durou 24 horas")

elif duracao_jogo < 0:
    duracao_jogo += 24
    print(f"O jogo durou {duracao_jogo} horas")

else:
    print(f"O jogo durou {duracao_jogo} horas")