nota1 = float(input("Digite a primeira nota do estudante: "))
nota2 = float(input("Digite a segunda nota do estudante: "))
nota3 = float(input("Digite a terceira nota do estudante: "))
media_exercicios = float(input("Digite a médias dos exercícios do estudante: "))

media_aproveitamento = ((nota1 + (nota2 * 2) + (nota3 * 3) + media_exercicios) / 7)

if nota1 < 0 or nota2 < 0 or nota3 < 0 or media_exercicios < 0:
    print("Notas inválidas")

else:

    if media_aproveitamento >= 9:
        print(f"O estudante tem o conceito 'A' com média de aproveitamento igual à: {media_aproveitamento:.2f}")

    elif media_aproveitamento >= 7.5:
        print(f"O estudante tem o conceito 'B' com média de aproveitamento igual à: {media_aproveitamento:.2f}")

    elif media_aproveitamento >= 6:
        print(f"O estudante tem o conceito 'C' com média de aproveitamento igual à: {media_aproveitamento:.2f}")

    else:
        print(f"O estudante tem o conceito 'D' com média de aproveitamento igual à: {media_aproveitamento:.2f}")

