def criar_cadastro():
    dados = {}

    quantidade = int(input("Quantos dados você quer cadastrar? "))

    for i in range(quantidade):
        chave = input("Digite o nome do campo: ")
        valor = input(f"Digite o valor de {chave}: ")

        dados[chave] = valor

    print("Cadastro Final: ", dados)

criar_cadastro()