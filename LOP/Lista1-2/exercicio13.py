num_conta = int(input("Digite o número da sua conta: "))
saldo = float(input("Digite seu saldo: "))
debito = float(input("Digite seu debito: "))
credito = float(input("Digite seu credito: "))

saldo_atual = (saldo - debito + credito)

if saldo_atual < 0:
    print(f"A conta º{num_conta}, tem saldo negativado de: R$ {saldo_atual}")

elif saldo_atual > 0:
    print(f"A conta nº{num_conta}, tem saldo positivo de: R$ {saldo_atual}")

else:
    print(f"A conta º{num_conta}, tem saldo R$ 0")