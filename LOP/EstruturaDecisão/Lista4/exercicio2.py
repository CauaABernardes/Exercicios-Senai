data_inserida = input("Digite uma data qualquer seguindo este formato (dd/mm/aaaa): ")

dia = (data_inserida[0] + data_inserida[1])
mes = (data_inserida[3] + data_inserida[4])
ano = (data_inserida[6] + data_inserida[7] + data_inserida[8] + data_inserida[9])

if mes in ["01", "03", "05", "07", "08", "10", "12"]:
    if int(dia) <= 0:
        print("Data inválida")

    elif int(dia) <= 31:
        print("Data válida")

    else:
        print("Data inválida")

elif mes in ["04", "06", "09", "11"]:
    if int(dia) <= 0:
        print("Data inválida")

    elif int(dia) <= 30:
        print("Data válida")

    else:
        print("Data inválida")

elif mes == '02':

    if int(dia) <= 0:
        print("Data inválida")

    elif int(dia) <= 28:
        print("Data válida")

    else:
        if int(ano) % 100 == 0:

            if int(ano) % 400 == 0:
                print("Data válida")

            else:
                print("Data inválida")

        elif int(ano) % 4 == 0:
            print("Data válida")

        else:
            print("Data inválida")

else:
    print("Digitação incorreta")