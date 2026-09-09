import json

def cadastro_dinamico():
    dados = {}

    numero_de_info = int(input("Quantos dados deseja cadastrar? "))

    for dado in range(numero_de_info):
        nome_chave = input("Digite o nome do campo: ").lower()
        valor = input("Digite o valor: ")

        if nome_chave == "idade":
            valor = int(valor)

        dados[nome_chave] = valor

    print(json.dumps(dados, indent=4))

cadastro_dinamico()