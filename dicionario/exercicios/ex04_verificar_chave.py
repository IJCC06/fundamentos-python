def verificar_chave():
    cadastro = {
        "nome": "Gabriel",
        "idade": 16,
        "email": "ga010101@gmail.com",
        "endereco": "Rua das Flores, 123",
        "telefone": "19 99342-2561"
    }

    chave_verificacao = (input("Qual chave você quer verificar? ").lower()) in cadastro

    if chave_verificacao:
        print("Chave Encontrada!")
    else:
        print("Chave não Encontrada!")

verificar_chave()