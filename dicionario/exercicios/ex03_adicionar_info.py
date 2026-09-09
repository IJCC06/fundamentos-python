import json

def adicionar_informacaoes():
    cadastro = {
        "nome": "Gabriel",
        "idade": 16
    }

    cadastro["email"] = input("Digite seu email: ")
    cadastro["endereco"] = input("Digite seu endereço: ")
    cadastro["telefone"] = input("Digite seu telefone com DDD: ")

    print("\nDados Cadastrados!")
    print("Novo Cadastro: ", json.dumps(cadastro, indent=4))

adicionar_informacaoes()