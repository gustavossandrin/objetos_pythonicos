"""
contrua uma função de ordenação que ordene os alunos por nota. Se houver empate em nota, o nome deverá
definir a ordem

>>> import operator
>>> alunos = [('gustavo', 6), ('guilherme', 8), ('jessica', 4), ('gustavo sandrin', 8), ('andrey', 8)]
>>> alunos.sort(key=operator.itemgetter(1, 0))
>>> alunos
[('jessica', 4), ('gustavo', 6), ('andrey', 8), ('guilherme', 8), ('gustavo sandrin', 8)]

"""
alunos = [('gustavo', 6), ('guilherme', 8), ('jessica', 4), ('gustavo sandrin', 8), ('andrey', 8), ('andrey', 6)]


def ordenar_nota_nome(aluno):
    nome, nota = aluno
    return nota, nome


alunos.sort(key=ordenar_nota_nome)
print(alunos)
