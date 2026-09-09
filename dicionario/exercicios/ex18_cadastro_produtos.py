import json

def menu():
    opcoes = {
        "1": cadastrar,
        "2": listar,
        "3": atualizar,
        "4": remover
    }

    while True:
        print("\n======SISTEMA DE ESTOQUE======")
        print("1 - Cadastrar um Produto")
        print("2 - Listar Produtos")
        print("3 - Buscar Produto")
        print("4 - Atualizar Estoque")
        print("5 - Remover Produto")
        print("0 - Sair")

        opcao = input("Digite sua opção: ")