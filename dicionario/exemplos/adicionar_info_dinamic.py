def cadastrar_aluno():
    aluno = {}

    aluno["nome"] = input("Digite o nome do aluno: ")
    aluno["idade"] = int(input("Digite a idade: "))
    aluno["curso"] = input("Qual o curso do aluno: ")
    aluno["email"] = input("Digite o e-mail: ")

    print(f"Dados Cadastrados! Novo Aluno: {aluno}")

cadastrar_aluno()