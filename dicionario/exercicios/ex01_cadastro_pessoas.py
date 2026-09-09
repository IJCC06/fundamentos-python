def cadastro_de_pessoas():
    ficha = {}

    ficha["nome"] = input("Digite seu nome: ")
    ficha["idade"] = int(input("Digite sua idade: "))
    ficha["telefone"] = input("Digite seu telefone com o DDD: ")

    ficha["endereco"] = {}
    ficha["endereco"]["cidade"] = input("Digite sua cidade: ")
    ficha["endereco"]["rua"] = input("Digite o nome da rua: ")
    ficha["endereco"]["numero"] = int(input("Digite o número da casa: "))

    print("Cadastro Concluído!")
    print(f"Nome: {ficha["nome"]}")
    print(f"Idade: {ficha["idade"]}")
    print(f"Telefone: {ficha["telefone"]}")
    print(f"Endereço: Rua {ficha["endereco"]["rua"]}, {ficha["endereco"]["numero"]} - {ficha["endereco"]["cidade"]}")

cadastro_de_pessoas()