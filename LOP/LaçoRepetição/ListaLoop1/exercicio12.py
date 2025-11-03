num_alunos = int(input("Digite quantos alunos existem na turma: "))

media_alunos = 0

for i in range(1, num_alunos + 1):
    nota = float(input(f"Digite a nota do {i}º aluno: "))
    media_alunos += nota

media_alunos = media_alunos / num_alunos

print(f"A média total de notas, dos aluno é de: {media_alunos:.2f}")