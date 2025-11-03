num = int(input("Digite um número: "))
e_primo = True

if num == 2:
    e_primo = True

elif num % 2 == 0:
    e_primo = False

else:
    for i in range(2, num//2):
        if num % i == 0:
            e_primo = False

if e_primo:
    print(f"O número {num} é primo")

else:
    print(f"O número {num} não é primo")