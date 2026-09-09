import json
from textwrap import indent


def remover_informacoes():
    dados = {
        "nome": "João",
        "idade": 34,
        "cargo": "Auxiliar de RH",
        "salario": 2400.0,
        "telefone": "19 99241-0283"
    }

    print(f"Dados do Funcionário antigos: ", json.dumps(dados, indent=4))

    telefone = dados.pop("telefone")
    print(f"Telefone: {telefone}")

    print(f"Dados do Funcionário atualizados: ", json.dumps(dados, indent=4))

remover_informacoes()