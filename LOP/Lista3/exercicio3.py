valor_casa = float(input("Digite o valor da casa: "))
salario_cliente = float(input("Digite o seu salário: "))
tempo_prestacao = int(input("Digite em quantos anos você deseja pagar a casa: "))

valor_max_cliente = salario_cliente * 0.3

if valor_casa <= 0 or salario_cliente <= 0:
    print("Valores inválidos")

elif tempo_prestacao == 0:

     if valor_casa > valor_max_cliente:
         print("Você não pode comprar à vista, tente com empréstimo ou parcelamento")
     else:
         print("Compra do imóvel concluída\nObrigado por comprar conosco")

else:
    prestacao_casa_mensal = valor_casa // (tempo_prestacao * 12)

    if prestacao_casa_mensal > valor_max_cliente:
        print("O empréstimo foi negado devido ter exedido o orçamento previsto pelo cliente")

    else:
        print(f"Empréstimo concedido com sucesso\nO valor mensal das prestações é de: R${prestacao_casa_mensal}")