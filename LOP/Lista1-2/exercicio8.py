ano = int(input("Digite um ano qualquer: "))

if ano % 100 == 0:
    
    if ano % 400 == 0:
        print("O ano é bissexto")

    else:
        print("O ano não é bissexto")

elif ano % 4 == 0:
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")