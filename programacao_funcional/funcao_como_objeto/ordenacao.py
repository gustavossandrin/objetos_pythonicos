alunos = [('gustavo', 6), ('guilherme', 3), ('jessica', 4)]

alunos.sort(key=lambda aluno: aluno[1])

print(alunos)


def por_nome(aluno):
    return aluno[0]


alunos = sorted(alunos, key=por_nome)
print(alunos)
