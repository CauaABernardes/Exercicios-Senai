print("Digite os tempos-padrão em minutos das 3 fases:")
padrao1 = float(input("Fase 1: "))
padrao2 = float(input("Fase 2: "))
padrao3 = float(input("Fase 3: "))

print("\nDados das equipes: ")

num_inscricao = int(input("Número de inscrição: "))

while num_inscricao != 9999:
    tempo1 = float(input("Tempo na Fase 1: "))
    tempo2 = float(input("Tempo na Fase 2: "))
    tempo3 = float(input("Tempo na Fase 3: "))

    total_pontos = 0

    for i in range(1, 4):
        if i == 1:
            diferenca = padrao1 - tempo1

            if diferenca < 0:
                diferenca = -diferenca

        elif i == 2:
            diferenca = padrao2 - tempo2

            if diferenca < 0:
                diferenca = -diferenca
        else:
            diferenca = padrao3 - tempo3

            if diferenca < 0:
                diferenca = -diferenca

        if diferenca < 3:
            pontos = 100
        elif diferenca <= 5:
            pontos = 80
        else:
            pontos = 80 - ((diferenca - 5) / 5)

        total_pontos += pontos

        print(f"\nEtapa {i}: {pontos:.2f} pontos")

    print(f"\nEquipe {num_inscricao} - Total de pontos: {total_pontos:.2f}\n")

    print("Próxima equipe:")

    num_inscricao = int(input("Número de inscrição: "))

print("\nFim das inscrições.")
