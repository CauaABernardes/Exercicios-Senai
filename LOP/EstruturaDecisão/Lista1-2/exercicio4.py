opcao = input("Digite 'C' para converter uma temperatura de Celsius para Fahrenheit\nOu digite 'F' para converter uma temperatura de Fahrenheit para Celsius: ")

if opcao == "C":
    temp_c = float(input("Digite a temperatura que será convertida em Celsius: "))
    if temp_c < -273.15:
        print("Não existe temperatura abaixo do zero absoluto")
    else:
        temp_f = ((temp_c * 1.8) + 32)
        print(f"A temperatura {temp_c}°C em Fahrenheit é: {temp_f}ºF")
elif opcao == "F":
    temp_f = float(input("Digite a temperatura que será convertida em Celsius: "))
    if temp_f < -459.67:
        print("Não existe temperatura abaixo do zero absoluto")
    else:
        temp_c = ((temp_f - 32) / 1.8)
        print(f"A temperatura {temp_f}°F em Celsius é: {temp_c}ºC")
else:
    print("Opção inválida")