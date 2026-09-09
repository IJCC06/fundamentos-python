import json

def limpar_cadastro():
    dados = {
        "nome": "João",
        "idade": 34,
        "cargo": "Auxiliar de RH",
        "salario": 2400.0,
        "telefone": "19 99241-0283"
    }
    del dados["telefone"]

    print(json.dumps(dados, indent=4))

limpar_cadastro()