import json

def cadastrar_alunos():
    alunos = []

    for aluno in range(5):
        cadastro_aluno = {}

        cadastro_aluno["nome"] = input("\nDigite o nome do aluno: ")
        cadastro_aluno["idade"] = int(input("Digite a idade do aluno: "))
        cadastro_aluno["nota"] = float(input("Digite a nota do aluno: "))

        alunos.append(cadastro_aluno)

    print("Cadastro Cadastrados:")
    print(json.dumps(alunos, indent=4))

cadastrar_alunos()