numero = int(input("Digite um número inteiro positivo menor que 1000: "))

if numero >= 1000:
    print("Número inválido")

else:
    centena = (numero // 100)
    dezena = ((numero // 10) - (centena * 10) )
    unidade = (numero - (centena * 100) - (dezena * 10))

    if centena == 1:
        if dezena == 1:
            if unidade == 1:
                print(f"O número {numero} tem: {centena} centena, {dezena} dezena e {unidade} unidade")

            elif unidade == 0:
                print(f"O número {numero} tem: {centena} centena e {dezena} dezena")

            else:
                print(f"O número {numero} tem: {centena} centena, {dezena} dezena e {unidade} unidades")

        elif dezena == 0:
            if unidade == 1:
                print(f"O número {numero} tem: {centena} centena e {unidade} unidade")

            elif unidade == 0:
                print(f"O número {numero} tem: {centena} centena")

            else:
                print(f"O número {numero} tem: {centena} centena e {unidade} unidades")

        else:
            if unidade == 1:
                print(f"O número {numero} tem: {centena} centena, {dezena} dezenas e {unidade} unidade")

            elif unidade == 0:
                print(f"O número {numero} tem: {centena} centena e {dezena} dezenas")

            else:
                print(f"O número {numero} tem: {centena} centena, {dezena} dezenas e {unidade} unidades")

    elif centena == 0:
        if dezena == 1:
            if unidade == 1:
                print(f"O número {numero} tem: {dezena} dezena e {unidade} unidade")

            elif unidade == 0:
                print(f"O número {numero} tem: {dezena} dezena")

            else:
                print(f"O número {numero} tem: {dezena} dezena e {unidade} unidades")

        elif dezena == 0:
            if unidade == 1:
                print(f"O número {numero} tem: {unidade} unidade")

            else:
                print(f"O número {numero} tem: {unidade} unidades")

        else:
            if unidade == 1:
                print(f"O número {numero} tem: {centena} centena, {dezena} dezenas e {unidade} unidade")

            elif unidade == 0:
                print(f"O número {numero} tem: {centena} centena e {dezena} dezenas")

            else:
                print(f"O número {numero} tem: {centena} centena, {dezena} dezenas e {unidade} unidades")

    else:
        if dezena == 1:
            if unidade == 1:
                print(f"O número {numero} tem: {centena} centenas, {dezena} dezena e {unidade} unidade")

            elif unidade == 0:
                print(f"O número {numero} tem: {centena} centenas e {dezena} dezena")

            else:
                print(f"O número {numero} tem: {centena} centenas, {dezena} dezena e {unidade} unidades")

        elif dezena == 0:
            if unidade == 1:
                print(f"O número {numero} tem: {centena} centenas e {unidade} unidade")

            elif unidade == 0:
                print(f"O número {numero} tem: {centena} centenas")

            else:
                print(f"O número {numero} tem: {centena} centenas e {unidade} unidades")

        else:
            if unidade == 1:
                print(f"O número {numero} tem: {centena} centenas, {dezena} dezenas e {unidade} unidade")

            elif unidade == 0:
                print(f"O número {numero} tem: {centena} centenas e {dezena} dezenas")

            else:
                print(f"O número {numero} tem: {centena} centenas, {dezena} dezenas e {unidade} unidades")
