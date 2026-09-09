def consultar_cliente():
    cliente = {
        "nome": "João",
        "idade": 25,
        "email": "joao@email.com",
        "cidade": "São Paulo"
    }

    informacao = input("Digite a informação que deseja consultar: ")

    resultado = cliente.get(informacao)

    if resultado is not None:
        print("Informação:", resultado)
    else:
        print("Informação não encontrada.")


consultar_cliente()