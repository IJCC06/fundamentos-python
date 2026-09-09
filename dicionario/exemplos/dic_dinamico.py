import json

def calcular_media(notas):
    return sum(notas) / len(notas)

def cadastrar_novos_alunos():
    aluno = {}

    aluno["nome"] = input("Digite o nome do aluno: ")
    aluno["idade"] = int(input("Digite a idade do aluno: "))
    aluno["curso"] = input("Digite o nome do curso: ")
    aluno["notas"] = []

    for nota in range(4):
        aluno["notas"].append(float(input(f"Digite a nota {nota + 1}: ")))
    
    aluno["endereco"] = {}
    aluno["endereco"]["cidade"] = input("Digite a cidade do aluno: ")
    aluno["endereco"]["rua"] = input("Digite o nome da rua: ")
    aluno["endereco"]["numero"] = int(input("Digite o número da casa: "))
    aluno["endereco"]["telefone"] = input("Digite o telefone com DDD: ")

    aluno["media"] = calcular_media(aluno["notas"])
    print("Aluno Cadastrado!", json.dumps(aluno, indent=1))

cadastrar_novos_alunos()