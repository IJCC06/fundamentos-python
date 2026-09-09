import json

def cadastro_de_notas():
    dados = {}

    dados["nome"] = input("Digite o nome do aluno: ")
    dados["notas"] = []

    for nota in range(3):
        dados["notas"].append(float(input(f"Digite a nota {nota + 1}: ")))

    dados["media"] = sum(dados["notas"]) / len(dados["notas"])

    print(f"Notas = {dados["notas"]}")
    print(f"Média = {dados["media"]}")

cadastro_de_notas()