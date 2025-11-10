num_anterior = 0
num_atual = 1
num_atual_aux = num_atual

enensimo_desejado = int(input("Digite o enésimo números da sequência de Fibonacci: "))

for _ in range(enensimo_desejado):
    print(num_atual)
    num_atual += num_anterior
    num_anterior = num_atual_aux
    num_atual_aux = num_atual
