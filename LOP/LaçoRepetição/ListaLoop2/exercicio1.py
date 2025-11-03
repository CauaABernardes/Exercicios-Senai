import random as rd

nums_divisiveis_por_3 = []
nums_maiores_que_5 = []

for i in range (0, 20):
    num_aleatorio = rd.randint(0,10)
    if num_aleatorio > 5:
        nums_maiores_que_5.append((num_aleatorio))
    if num_aleatorio % 3 == 0:
        nums_divisiveis_por_3.append(num_aleatorio)
    print(f"Número sorteado: {num_aleatorio}")

print(f"Os números sorteados que são maiores do que 5 são: {nums_maiores_que_5}")
print(f"Os números sorteados que são divisíveis por 3 são: {nums_divisiveis_por_3}")